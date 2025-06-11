(function() {
  'use strict';

  // Global functions
  window.toggleNav = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    const navBloom = document.getElementById('navBloom');
    if (!navBloom) return;
    
    navBloom.classList.toggle('open');
    document.body.style.overflow = '';
    document.body.classList.remove('nav-open');
  };

  window.toggleTheme = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    
    try {
      localStorage.setItem('theme', newTheme);
    } catch(e) {}
  };

  window.scrollToTop = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Initialize when DOM is ready
  function init() {
    // Initialize theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);

    // Get elements
    const avatar = document.querySelector('.return-avatar');
    const quietReturn = document.getElementById('quietReturn');
    const navBloom = document.getElementById('navBloom');
    
    if (!avatar || !quietReturn || !navBloom) {
      console.error('Navigation elements not found');
      return;
    }

    // CRITICAL iOS FIX: Use touchstart for iOS devices
    const isIOS = /iPhone|iPad|iPod/.test(navigator.userAgent);
    
    if (isIOS || 'ontouchstart' in window) {
      // For iOS/touch devices, use touchstart
      avatar.addEventListener('touchstart', function(e) {
        e.preventDefault(); // Prevent the default touch behavior
        toggleNav(e);
      }, { passive: false });
    } else {
      // For desktop, use click
      avatar.addEventListener('click', toggleNav);
    }
    
    // Make avatar explicitly tappable
    avatar.style.cursor = 'pointer';
    avatar.style.WebkitTapHighlightColor = 'transparent';
    avatar.style.userSelect = 'none';
    avatar.style.WebkitUserSelect = 'none';
    avatar.style.WebkitTouchCallout = 'none';

    // Handle navigation item clicks
    document.addEventListener('click', function(e) {
      // Return to top
      if (e.target.classList.contains('nav-item') && e.target.textContent.includes('Return to top')) {
        e.preventDefault();
        scrollToTop();
      }
      
      // Theme toggle
      if (e.target.classList.contains('theme-toggle-menu') || 
          e.target.parentElement?.classList.contains('theme-toggle-menu')) {
        e.preventDefault();
        toggleTheme();
      }
      
      // Close menu when clicking outside
      if (navBloom.classList.contains('open') && !quietReturn.contains(e.target)) {
        navBloom.classList.remove('open');
      }
    });

    // Prevent menu from closing when clicking inside
    navBloom.addEventListener('click', function(e) {
      e.stopPropagation();
    });

    // Scroll visibility
    let scrollTimer;
    window.addEventListener('scroll', function() {
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(function() {
        const scrolled = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrolled > 300) {
          quietReturn.classList.add('visible');
        } else {
          quietReturn.classList.remove('visible');
          navBloom.classList.remove('open');
        }
      }, 50);
    }, { passive: true });
  }

  // Start initialization
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();