(function() {
  'use strict';

  // Make functions globally accessible
  window.toggleNav = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    const navBloom = document.getElementById('navBloom');
    if (!navBloom) return;
    
    navBloom.classList.toggle('open');
    
    // Never block scrolling on any device
    document.body.style.overflow = '';
    document.body.classList.remove('nav-open');
  };

  window.toggleTheme = function() {
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    
    // Update all theme labels
    document.querySelectorAll('.theme-label').forEach(label => {
      label.textContent = newTheme === 'light' ? 'Dark mode' : 'Light mode';
    });
    
    // Store preference (wrapped in try-catch for iOS)
    try {
      localStorage.setItem('theme', newTheme);
    } catch(e) {
      console.log('localStorage not available');
    }
  };

  // Mobile header navigation toggle
  window.toggleHeaderNav = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    const headerNavBloom = document.getElementById('headerNavBloom');
    if (!headerNavBloom) return;
    
    headerNavBloom.classList.toggle('open');
  };

  // Initialize on DOM ready
  document.addEventListener('DOMContentLoaded', function() {
    // Set initial theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    
    // Update theme labels
    document.querySelectorAll('.theme-label').forEach(label => {
      label.textContent = savedTheme === 'light' ? 'Dark mode' : 'Light mode';
    });
    
    // Quiet return navigation visibility on scroll
    const quietReturn = document.getElementById('quietReturn');
    if (quietReturn) {
      let lastScroll = 0;
      
      window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        if (currentScroll > 300) {
          quietReturn.classList.add('visible');
        } else {
          quietReturn.classList.remove('visible');
          // Close menu when scrolling to top
          const navBloom = document.getElementById('navBloom');
          if (navBloom) {
            navBloom.classList.remove('open');
          }
        }
        
        lastScroll = currentScroll;
      });
    }
    
    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
      const navBloom = document.getElementById('navBloom');
      const quietReturn = document.getElementById('quietReturn');
      const headerNavBloom = document.getElementById('headerNavBloom');
      const quietHeader = document.querySelector('.quiet-header');
      
      // Close desktop navigation
      if (navBloom && navBloom.classList.contains('open')) {
        if (!quietReturn.contains(e.target)) {
          navBloom.classList.remove('open');
        }
      }
      
      // Close mobile navigation
      if (headerNavBloom && headerNavBloom.classList.contains('open')) {
        if (!quietHeader.contains(e.target) && !headerNavBloom.contains(e.target)) {
          headerNavBloom.classList.remove('open');
        }
      }
    });
    
    // Handle touch events for mobile
    if ('ontouchstart' in window) {
      const avatar = document.querySelector('.return-avatar');
      if (avatar) {
        avatar.addEventListener('touchend', function(e) {
          e.preventDefault();
          toggleNav(e);
        });
      }
    }
  });
})();