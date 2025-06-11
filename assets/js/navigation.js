(function() {
  'use strict';

  // Make toggleNav globally accessible
  window.toggleNav = function(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    console.log('toggleNav called'); // Debug log
    
    const navBloom = document.getElementById('navBloom');
    if (!navBloom) {
      console.log('navBloom not found');
      return;
    }
    
    navBloom.classList.toggle('open');
    console.log('Nav is now:', navBloom.classList.contains('open') ? 'open' : 'closed');
    
    // Never block scrolling
    document.body.style.overflow = '';
    document.body.classList.remove('nav-open');
  };

  // Theme toggle function
  window.toggleTheme = function() {
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    
    // Update all theme labels
    document.querySelectorAll('.theme-label').forEach(label => {
      label.textContent = newTheme === 'light' ? 'Dark mode' : 'Light mode';
    });
    
    // Store preference
    try {
      localStorage.setItem('theme', newTheme);
    } catch(e) {
      console.log('localStorage not available');
    }
  };

  // Initialize when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    console.log('Navigation script loaded');
    
    // Get the avatar element
    const avatar = document.querySelector('.return-avatar');
    if (!avatar) {
      console.log('Avatar not found');
      return;
    }
    
    // Remove any existing onclick attribute
    avatar.removeAttribute('onclick');
    
    // Add both click and touch listeners
    avatar.addEventListener('click', toggleNav, { passive: false });
    avatar.addEventListener('touchend', function(e) {
      e.preventDefault(); // Prevent ghost clicks
      toggleNav(e);
    }, { passive: false });
    
    console.log('Event listeners attached to avatar');
    
    // Handle scroll visibility
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
    
    // Close menu when clicking/tapping outside
    document.addEventListener('click', function(e) {
      const navBloom = document.getElementById('navBloom');
      const quietReturn = document.getElementById('quietReturn');
      
      if (navBloom && navBloom.classList.contains('open')) {
        if (!quietReturn.contains(e.target)) {
          navBloom.classList.remove('open');
        }
      }
    });
    
    // Also handle touch events for closing
    document.addEventListener('touchstart', function(e) {
      const navBloom = document.getElementById('navBloom');
      const quietReturn = document.getElementById('quietReturn');
      
      if (navBloom && navBloom.classList.contains('open')) {
        if (!quietReturn.contains(e.target)) {
          navBloom.classList.remove('open');
        }
      }
    });
    
    // Set initial theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    
    // Update theme labels
    document.querySelectorAll('.theme-label').forEach(label => {
      label.textContent = savedTheme === 'light' ? 'Dark mode' : 'Light mode';
    });
  });
})();