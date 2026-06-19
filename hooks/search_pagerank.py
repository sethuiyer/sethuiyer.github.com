"""Inject internal-link PageRank boosts into Material for MkDocs search.

MkDocs Material builds ``search/search_index.json`` with one document per page
section. Its search worker passes ``doc.boost`` through to Lunr, so a build hook
can compute page-level authority from Markdown interlinks and apply a modest
ranking boost without overriding the frontend search implementation.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from urllib.parse import unquote, urlparse


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def on_post_build(config, **kwargs) -> None:
    docs_dir = Path(config["docs_dir"]).resolve()
    site_dir = Path(config["site_dir"]).resolve()
    index_path = site_dir / "search" / "search_index.json"

    if not index_path.exists():
        return

    pages = _discover_pages(docs_dir)
    if not pages:
        return

    graph = _build_link_graph(docs_dir, pages)
    ranks = _pagerank(graph)
    normalized = _normalize(ranks)

    with index_path.open(encoding="utf-8") as f:
        search_index = json.load(f)

    for doc in search_index.get("docs", []):
        page_url = _page_url_from_location(doc.get("location", ""))
        rank = normalized.get(page_url, 0.0)

        # Keep PageRank as a gentle prior. Text relevance should still dominate.
        boost = 0.85 + 0.45 * math.sqrt(rank)
        doc["boost"] = round(boost, 6)
        doc["pagerank"] = round(rank, 6)

    search_index.setdefault("config", {})["pagerank"] = {
        "enabled": True,
        "damping": 0.85,
        "boost_min": 0.85,
        "boost_max": 1.30,
        "pages": len(pages),
    }

    with index_path.open("w", encoding="utf-8") as f:
        json.dump(search_index, f, ensure_ascii=False, separators=(",", ":"))


def _discover_pages(docs_dir: Path) -> dict[Path, str]:
    pages: dict[Path, str] = {}
    for path in docs_dir.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(docs_dir).parts):
            continue
        pages[path.resolve()] = _source_path_to_url(path, docs_dir)
    return pages


def _source_path_to_url(path: Path, docs_dir: Path) -> str:
    rel = path.relative_to(docs_dir)
    if rel.name == "index.md":
        parent = rel.parent.as_posix()
        return "" if parent == "." else f"{parent}/"
    return f"{rel.with_suffix('').as_posix()}/"


def _build_link_graph(docs_dir: Path, pages: dict[Path, str]) -> dict[str, set[str]]:
    path_by_resolved = {path: url for path, url in pages.items()}
    graph = {url: set() for url in pages.values()}

    for path, source_url in pages.items():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for raw_target in LINK_RE.findall(text):
            target_path = _resolve_markdown_target(raw_target, path.parent, docs_dir)
            if target_path is None:
                continue
            target_url = path_by_resolved.get(target_path)
            if target_url is not None and target_url != source_url:
                graph[source_url].add(target_url)

    return graph


def _resolve_markdown_target(raw_target: str, base_dir: Path, docs_dir: Path) -> Path | None:
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

    return candidate


def _pagerank(
    graph: dict[str, set[str]],
    damping: float = 0.85,
    iterations: int = 60,
    tolerance: float = 1e-12,
) -> dict[str, float]:
    nodes = list(graph)
    n = len(nodes)
    if n == 0:
        return {}

    ranks = {node: 1.0 / n for node in nodes}
    base = (1.0 - damping) / n

    for _ in range(iterations):
        next_ranks = {node: base for node in nodes}
        dangling_rank = sum(ranks[node] for node in nodes if not graph[node])
        dangling_share = damping * dangling_rank / n

        for node in nodes:
            next_ranks[node] += dangling_share

        for source, targets in graph.items():
            if not targets:
                continue
            share = damping * ranks[source] / len(targets)
            for target in targets:
                next_ranks[target] += share

        delta = sum(abs(next_ranks[node] - ranks[node]) for node in nodes)
        ranks = next_ranks
        if delta < tolerance:
            break

    return ranks


def _normalize(ranks: dict[str, float]) -> dict[str, float]:
    if not ranks:
        return {}
    low = min(ranks.values())
    high = max(ranks.values())
    if high == low:
        return {key: 1.0 for key in ranks}
    return {key: (value - low) / (high - low) for key, value in ranks.items()}


def _page_url_from_location(location: str) -> str:
    return location.split("#", 1)[0]
