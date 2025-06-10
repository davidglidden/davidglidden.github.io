(function() {
  'use strict';
  
  // Initialize theme
  function initTheme() {
    const theme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', theme);
  }
  
  // Theme toggle function
  window.toggleTheme = function() {
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Update theme label if it exists
    const themeLabel = document.querySelector('.theme-label');
    if (themeLabel) {
      themeLabel.textContent = 'Theme: ' + newTheme;
    }
  }
  
  // Scroll to top
  window.scrollToTop = function(e) {
    if (e) e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  
  // Simple navigation toggle
  window.toggleNavMenu = function() {
    const navBloom = document.getElementById('navBloom');
    if (navBloom) {
      const isOpen = navBloom.style.display === 'block';
      navBloom.style.display = isOpen ? 'none' : 'block';
      
      // Position menu near avatar
      if (!isOpen) {
        const avatar = document.querySelector('.return-avatar');
        if (avatar) {
          const rect = avatar.getBoundingClientRect();
          navBloom.style.position = 'fixed';
          navBloom.style.bottom = (window.innerHeight - rect.top + 10) + 'px';
          navBloom.style.right = '20px';
          navBloom.style.zIndex = '999999';
        }
      }
    }
  }
  
  // Initialize navigation
  function initNavigation() {
    const quietReturn = document.getElementById('quietReturn');
    
    if (!quietReturn) {
      console.error('Navigation container not found');
      return;
    }
    
    // Show/hide on scroll
    let scrollTimeout;
    window.addEventListener('scroll', function() {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(function() {
        const scrolled = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrolled > 200) {
          quietReturn.style.opacity = '1';
          quietReturn.style.transform = 'translateY(0)';
        } else {
          quietReturn.style.opacity = '0';
          quietReturn.style.transform = 'translateY(20px)';
          // Also hide menu when scrolling to top
          const navBloom = document.getElementById('navBloom');
          if (navBloom) {
            navBloom.style.display = 'none';
          }
        }
      }, 50);
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
      const quietReturn = document.getElementById('quietReturn');
      const navBloom = document.getElementById('navBloom');
      
      if (navBloom && !quietReturn.contains(e.target)) {
        navBloom.style.display = 'none';
      }
    });
    
    // Prevent menu from closing when clicking inside
    const navBloom = document.getElementById('navBloom');
    if (navBloom) {
      navBloom.addEventListener('click', function(e) {
        e.stopPropagation();
      });
    }
  }
  
  // Start when ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initTheme();
      initNavigation();
    });
  } else {
    initTheme();
    initNavigation();
  }
})();