"""Inject a "Recent Articles" widget into the MkDocs build.

This hook scans all Markdown files in the docs directory, sorts by
modification time and link authority (from the existing PageRank data),
and generates a recent articles section that gets injected into the homepage.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlparse

from mkdocs.structure.pages import Page


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EXCLUDE_DIRS = {".git", "assets", "stylesheets", "images", "javascript"}
ARTICLE_LIMIT = 6
WIDGET_MARKER = "<!-- latest-articles-widget -->"
# Cache for computed pages
_cached_pages: list[dict] = []


def on_config(config, **kwargs):
    """Precompute recent articles during config loading."""
    docs_dir = Path(config["docs_dir"]).resolve()

    pages = _discover_pages(docs_dir)
    if not pages:
        return config

    _build_link_graph(docs_dir, pages)
    scored_pages = _score_pages(pages)
    top_pages = sorted(scored_pages, key=lambda x: x["score"], reverse=True)[:ARTICLE_LIMIT]

    global _cached_pages
    _cached_pages = top_pages
    return config


def on_page_markdown(markdown: str, page: Page, config, **kwargs) -> str:
    """Inject recent articles into the homepage markdown."""
    global _cached_pages

    # Only inject into the homepage
    if page.file.src_uri != "index.md":
        return markdown

    if not _cached_pages:
        return markdown

    # Generate the widget markdown
    widget = _generate_widget_markdown(_cached_pages)

    if WIDGET_MARKER in markdown:
        return markdown.replace(WIDGET_MARKER, widget)

    # Fallback for older homepages without the explicit marker.
    return markdown.rstrip() + "\n\n" + widget


def on_post_build(config, **kwargs) -> None:
    """Also generate JSON for programmatic access."""
    docs_dir = Path(config["docs_dir"]).resolve()
    site_dir = Path(config["site_dir"]).resolve()

    pages = _discover_pages(docs_dir)
    if not pages:
        return

    _build_link_graph(docs_dir, pages)
    scored_pages = _score_pages(pages)
    top_pages = sorted(scored_pages, key=lambda x: x["score"], reverse=True)[:ARTICLE_LIMIT]

    # Generate JSON for JS
    json_path = site_dir / "recent-articles.json"
    json_data = {
        "generated": datetime.now().isoformat(),
        "articles": [
            {
                "title": p["title"],
                "url": p["url"],
                "category": p["category"],
                "date": p["date"],
            }
            for p in top_pages
        ]
    }

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)


def _discover_pages(docs_dir: Path) -> dict[Path, dict]:
    """Discover all markdown pages with their metadata."""
    pages: dict[Path, dict] = {}

    for path in docs_dir.rglob("*.md"):
        # Skip hidden dirs and certain directories
        rel_parts = path.relative_to(docs_dir).parts
        if any(part.startswith(".") for part in rel_parts):
            continue
        if any(excluded in rel_parts for excluded in EXCLUDE_DIRS):
            continue
        # Skip index.md (homepage)
        if path.name == "index.md":
            continue

        # Get modification time
        mtime = path.stat().st_mtime
        mdate = datetime.fromtimestamp(mtime)

        # Read title from first H1 or filename
        title = _extract_title(path)

        # Determine category from path
        category = _extract_category(path, docs_dir)

        pages[path.resolve()] = {
            "path": path,
            "src_uri": path.relative_to(docs_dir).as_posix(),
            "url": _source_path_to_url(path, docs_dir),
            "title": title,
            "category": category,
            "mtime": mtime,
            "mdate": mdate.strftime("%b %Y"),
            "inbound": 0,  # Will be computed
        }

    return pages


def _source_path_to_url(path: Path, docs_dir: Path) -> str:
    rel = path.relative_to(docs_dir)
    if rel.name == "index.md":
        parent = rel.parent.as_posix()
        return "" if parent == "." else f"{parent}/"
    return f"{rel.with_suffix('').as_posix()}/"


def _extract_title(path: Path) -> str:
    """Extract title from first H1 heading or filename."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        # Try first ## or # heading
        match = re.search(r"^#+\s+(.+)$", text, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception:
        pass

    # Fallback to filename
    return path.stem.replace("-", " ").replace("_", " ").title()


def _extract_category(path: Path, docs_dir: Path) -> str:
    """Extract category from path."""
    rel = path.relative_to(docs_dir)
    parts = rel.parts
    if len(parts) > 1:
        return parts[0].title()
    return "Docs"


def _build_link_graph(docs_dir: Path, pages: dict[Path, dict]) -> dict[str, set[str]]:
    """Build link graph to compute inbound links."""
    path_by_url = {p["url"]: path for path, p in pages.items()}
    urls = list(pages.values())
    graph = {url["url"]: set() for url in urls}

    for path, page in pages.items():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for raw_target in LINK_RE.findall(text):
                target_url = _resolve_target(raw_target, path.parent, docs_dir, path_by_url)
                if target_url and target_url != page["url"]:
                    graph[page["url"]].add(target_url)
        except Exception:
            continue

    # Count inbound links
    inbound_count = {url: 0 for url in graph}
    for source_urls in graph.values():
        for target_url in source_urls:
            if target_url in inbound_count:
                inbound_count[target_url] += 1

    # Update pages with inbound counts
    for page in pages.values():
        page_url = page.get("url", "")
        page["inbound"] = inbound_count.get(page_url, 0)

    return graph


def _resolve_target(raw_target: str, base_dir: Path, docs_dir: Path, url_map: dict) -> str | None:
    target = raw_target.strip().split()[0]
    parsed = urlparse(target)

    if parsed.scheme or parsed.netloc or target.startswith("#"):
        return None

    path_part = unquote(parsed.path)
    if not path_part:
        return None

    if path_part.endswith("/"):
        candidate = (base_dir / path_part / "index.md").resolve()
    else:
        candidate = (base_dir / path_part).resolve()
        if candidate.suffix == "":
            candidate = candidate.with_suffix(".md")

    try:
        candidate.relative_to(docs_dir)
    except ValueError:
        return None

    return url_map.get(candidate.resolve())


def _score_pages(pages: dict[Path, dict]) -> list[dict]:
    """Score pages: recency (70%) + link authority (30%)."""
    if not pages:
        return []

    # Normalize times
    times = [p["mtime"] for p in pages.values()]
    min_time, max_time = min(times), max(times)
    time_range = max_time - min_time if max_time > min_time else 1

    # Normalize inbound links
    inbounds = [p["inbound"] for p in pages.values()]
    max_in = max(inbounds) if inbounds else 1

    scored = []
    for page in pages.values():
        # Recency score (newer = higher)
        if time_range > 0:
            recency = (page["mtime"] - min_time) / time_range
        else:
            recency = 0.5

        # Authority score (more inbound = higher)
        authority = page["inbound"] / max_in if max_in > 0 else 0

        # Combined: 70% recency, 30% authority
        score = 0.98 * recency + 0.02 * authority

        scored.append({
            "src_uri": page["src_uri"],
            "url": page["url"],
            "title": page["title"],
            "category": page["category"],
            "date": page["mdate"],
            "inbound": page["inbound"],
            "score": score,
        })

    return scored


def _generate_widget_markdown(pages: list[dict]) -> str:
    """Generate markdown widget for homepage injection."""
    lines = [
        "## Latest 6",
        "",
        "Auto-generated from the knowledge base — sorted by recency and link authority.",
        "",
        "| Article | Date | Category |",
        "|:---|:---|:---|",
    ]

    for p in pages:
        title = p["title"][:55] + "..." if len(p["title"]) > 55 else p["title"]
        lines.append(f"| [{title}]({p['src_uri']}) | {p['date']} | {p['category']} |")

    return "\n".join(lines)
