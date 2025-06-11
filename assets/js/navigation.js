(function() {
  'use strict';

  // Global navigation toggle
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

  // Global theme toggle
  window.toggleTheme = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    
    document.querySelectorAll('.theme-label').forEach(label => {
      label.textContent = newTheme === 'light' ? 'Dark mode' : 'Light mode';
    });
    
    try {
      localStorage.setItem('theme', newTheme);
    } catch(e) {
      console.log('localStorage not available');
    }
  };

  // Global scroll to top
  window.scrollToTop = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Initialize everything when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    document.querySelectorAll('.theme-label').forEach(label => {
      label.textContent = savedTheme === 'light' ? 'Dark mode' : 'Light mode';
    });

    // Get elements
    const avatar = document.querySelector('.return-avatar');
    const quietReturn = document.getElementById('quietReturn');
    const navBloom = document.getElementById('navBloom');
    
    if (!avatar || !quietReturn || !navBloom) {
      console.error('Navigation elements not found');
      return;
    }

    // Avatar click handler - works on all devices
    avatar.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      toggleNav(e);
    }, true); // Use capturing phase for iOS
    
    // Make avatar explicitly clickable for iOS
    avatar.style.cursor = 'pointer';
    avatar.style.WebkitTapHighlightColor = 'rgba(0,0,0,0.1)';
    avatar.style.touchAction = 'manipulation';

    // Handle all navigation item clicks
    document.addEventListener('click', function(e) {
      // Handle "Return to top" clicks
      if (e.target.classList.contains('nav-item') && e.target.textContent.includes('Return to top')) {
        e.preventDefault();
        scrollToTop();
      }
      
      // Handle theme toggle button clicks
      if (e.target.classList.contains('theme-toggle-menu') || 
          e.target.parentElement?.classList.contains('theme-toggle-menu')) {
        e.preventDefault();
        toggleTheme();
      }
      
      // Close menu when clicking outside
      if (navBloom.classList.contains('open') && !quietReturn.contains(e.target)) {
        navBloom.classList.remove('open');
      }
    }, true); // Use capturing

    // Prevent menu from closing when clicking inside
    navBloom.addEventListener('click', function(e) {
      e.stopPropagation();
    });

    // Scroll visibility handler
    let lastScroll = 0;
    window.addEventListener('scroll', function() {
      const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
      
      if (currentScroll > 300) {
        quietReturn.classList.add('visible');
      } else {
        quietReturn.classList.remove('visible');
        navBloom.classList.remove('open');
      }
      
      lastScroll = currentScroll;
    }, { passive: true });
  });
})();