(function() {
  'use strict';
  
  // Simple mobile-first navigation that WILL work
  
  // Theme functionality
  function initTheme() {
    const theme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', theme);
  }
  
  window.toggleTheme = function() {
    const currentTheme = document.body.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  }
  
  window.scrollToTop = function(e) {
    if (e) e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  
  // Navigation - simplified for mobile
  function initNavigation() {
    const quietReturn = document.getElementById('quietReturn');
    const navBloom = document.getElementById('navBloom');
    const returnAvatar = document.querySelector('.return-avatar');
    
    if (!quietReturn || !navBloom || !returnAvatar) {
      console.error('Navigation elements not found');
      return;
    }
    
    // Simple toggle function
    function toggleNav() {
      navBloom.classList.toggle('open');
      if (navBloom.classList.contains('open')) {
        document.body.classList.add('nav-open');
      } else {
        document.body.classList.remove('nav-open');
      }
    }
    
    // Show/hide on scroll
    let lastScroll = 0;
    window.addEventListener('scroll', function() {
      const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
      
      if (currentScroll > 200) {
        quietReturn.classList.add('visible');
      } else {
        quietReturn.classList.remove('visible');
        navBloom.classList.remove('open');
        document.body.classList.remove('nav-open');
      }
      
      lastScroll = currentScroll;
    });
    
    // Single event listener for avatar - works on ALL devices
    returnAvatar.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      toggleNav();
    });
    
    // Also add pointer events for better mobile support
    returnAvatar.style.cursor = 'pointer';
    returnAvatar.style.touchAction = 'manipulation';
    
    // Close nav when clicking outside
    document.addEventListener('click', function(e) {
      if (!quietReturn.contains(e.target)) {
        navBloom.classList.remove('open');
        document.body.classList.remove('nav-open');
      }
    });
    
    // Prevent closing when clicking inside nav
    navBloom.addEventListener('click', function(e) {
      e.stopPropagation();
    });
    
    // Make toggle function global
    window.toggleNav = toggleNav;
  }
  
  // Start when DOM is ready
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