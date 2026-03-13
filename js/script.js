// Vintage-inspired Portfolio JavaScript for Sethu Iyer

document.addEventListener('DOMContentLoaded', () => {
  // Fetch LeetCode stats dynamically
  const fetchLeetCodeStats = () => {
    const leetcodeProblems = document.getElementById('leetcode-problems');
    if (leetcodeProblems && typeof $ !== 'undefined') {
      // Using AllOrigins as a CORS proxy
      const proxyUrl = 'https://api.allorigins.win/raw?url=';
      const targetUrl = encodeURIComponent('https://leetcode.com/u/brobear/');

      $.ajax({
        url: proxyUrl + targetUrl,
        type: 'GET',
        dataType: 'html',
        success: function (data) {
          try {
            // Extract the solved problems count using regex
            const solvedMatch = data.match(/Solved (\d+)\//);
            if (solvedMatch && solvedMatch[1]) {
              leetcodeProblems.textContent = solvedMatch[1];
            }
          } catch (error) {
            console.error('Error parsing LeetCode data:', error);
          }
        },
        error: function (xhr, status, error) {
          console.error('Error fetching LeetCode stats:', error);
        }
      });
    }
  };

  // Try to fetch LeetCode stats
  setTimeout(fetchLeetCodeStats, 1000); // Delay to ensure jQuery is loaded

  // Animate sections on scroll
  const animateSections = () => {
    const sections = document.querySelectorAll('.animated-section');

    sections.forEach(section => {
      const sectionTop = section.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;

      if (sectionTop < windowHeight * 0.75) {
        section.style.opacity = '1';
        section.style.transform = 'translateY(0)';
      }
    });
  };

  // Initialize animations
  window.addEventListener('scroll', animateSections);
  animateSections(); // Run once on load

  // Vintage typing effect for bio text
  const bioText = document.getElementById('bio-text');
  if (bioText) {
    const text = bioText.textContent;
    bioText.textContent = '';

    let i = 0;
    const typeWriter = () => {
      if (i < text.length) {
        bioText.textContent += text.charAt(i);
        i++;
        setTimeout(typeWriter, 25);
      }
    };

    setTimeout(typeWriter, 1000);
  }

  // Project filter functionality
  const filterButtons = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Remove active class from all buttons
      filterButtons.forEach(btn => btn.classList.remove('active'));

      // Add active class to clicked button
      button.classList.add('active');

      const filter = button.getAttribute('data-filter');

      // Show/hide projects based on filter
      projectCards.forEach(card => {
        if (filter === 'all') {
          card.style.display = 'block';
        } else if (card.classList.contains(filter)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Form submission
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Simulate form submission
      const submitBtn = contactForm.querySelector('.form-button');
      const originalText = submitBtn.textContent;

      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending...';

      // Simulate API call
      setTimeout(() => {
        submitBtn.textContent = 'Message Sent!';
        contactForm.reset();

        // Reset button after 2 seconds
        setTimeout(() => {
          submitBtn.textContent = originalText;
          submitBtn.disabled = false;
        }, 2000);
      }, 1500);
    });
  }

  // Vintage-style scraps animation
  const scrapItems = document.querySelectorAll('.testimonial-box');

  scrapItems.forEach((item, index) => {
    item.style.transform = 'translateX(-30px)';
    item.style.opacity = '0';
    item.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
    item.style.transitionDelay = `${index * 0.1}s`;

    setTimeout(() => {
      item.style.transform = 'translateX(0)';
      item.style.opacity = '1';
    }, 500);
  });

  // Easter egg - vintage sound on logo click
  const logo = document.querySelector('.logo');
  if (logo) {
    logo.addEventListener('click', (e) => {
      if (e.altKey) {
        // Play vintage connection sound
        const sound = new Audio('https://www.myinstants.com/media/sounds/icq-message.mp3');
        sound.volume = 0.3;
        sound.play();

        // Add vintage flash effect
        document.body.classList.add('vintage-flash');
        setTimeout(() => {
          document.body.classList.remove('vintage-flash');
        }, 300);
      }
    });
  }

  // GitHub Stats
  async function fetchGitHubStats() {
    try {
      const response = await fetch('https://api.github.com/users/sethuiyer');
      const data = await response.json();

      // Get total stars
      const reposResponse = await fetch('https://api.github.com/users/sethuiyer/repos');
      const reposData = await reposResponse.json();
      const totalStars = reposData.reduce((acc, repo) => acc + repo.stargazers_count, 0);

      // Update stats in the DOM using existing elements
      const statsBar = document.querySelector('.stats-bar');
      if (statsBar) {
        statsBar.querySelector('.stat-item:nth-child(1) .stat-value').textContent = data.public_repos;
        statsBar.querySelector('.stat-item:nth-child(2) .stat-value').textContent = totalStars;
        statsBar.querySelector('.stat-item:nth-child(3) .stat-value').textContent = data.followers;
      }
    } catch (error) {
      console.error('Error fetching GitHub stats:', error);
    }
  }

  // Medium Feed
  async function fetchMediumFeed() {
    try {
      // Using a CORS proxy to avoid CORS issues with Medium's RSS feed
      const proxyUrl = 'https://api.allorigins.win/raw?url=';
      const mediumUrl = 'https://medium.com/feed/@sethuiyer';
      const response = await fetch(proxyUrl + encodeURIComponent(mediumUrl));
      const text = await response.text();

      // Parse XML
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(text, 'text/xml');

      // Get articles
      const items = xmlDoc.getElementsByTagName('item');

      // Update Medium link with RSS feed URL
      const mediumLink = document.querySelector('a[href*="medium.com"]');
      if (mediumLink) {
        mediumLink.href = mediumUrl;
      }

      // Update stats bar with article count
      const statsBar = document.querySelector('.stats-bar');
      if (statsBar) {
        statsBar.querySelector('.stat-item:nth-child(4) .stat-value').textContent = items.length;
      }
    } catch (error) {
      console.error('Error fetching Medium feed:', error);
    }
  }

  // Initialize when DOM is loaded
  fetchGitHubStats();
  fetchMediumFeed();

  // Refresh stats every 5 minutes
  setInterval(fetchGitHubStats, 300000);
  // Refresh Medium feed every hour
  setInterval(fetchMediumFeed, 3600000);

  // Mobile Menu Toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !menuToggle.contains(e.target)) {
        navMenu.classList.remove('active');
      }
    });
  }

  // Back to Top Button
  const backToTop = document.getElementById('back-to-top');

  if (backToTop) {
    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 300) {
        backToTop.style.display = 'flex';
      } else {
        backToTop.style.display = 'none';
      }
    });

    backToTop.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
}); 