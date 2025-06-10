(function() {
  'use strict';
  
  // Theme toggle functionality
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
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  
  window.toggleNav = function(e) {
    e.preventDefault();
    e.stopPropagation();
    const navBloom = document.getElementById('navBloom');
    navBloom.classList.toggle('open');
  }
  
  // Navigation functionality
  function initNavigation() {
    const quietReturn = document.getElementById('quietReturn');
    const navBloom = document.getElementById('navBloom');
    
    if (!quietReturn || !navBloom) return;
    
    // Show/hide quiet return on scroll
    let scrollTimeout;
    let lastScroll = 0;
    
    function handleScroll() {
      clearTimeout(scrollTimeout);
      
      scrollTimeout = setTimeout(() => {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        if (currentScroll > 200) {
          quietReturn.classList.add('visible');
        } else {
          quietReturn.classList.remove('visible');
          navBloom.classList.remove('open');
        }
        
        lastScroll = currentScroll;
      }, 50);
    }
    
    window.addEventListener('scroll', handleScroll, { passive: true });
    
    // Close nav when clicking outside
    document.addEventListener('click', function(e) {
      if (!quietReturn.contains(e.target)) {
        navBloom.classList.remove('open');
      }
    });
    
    // Prevent touch events from bubbling on mobile
    navBloom.addEventListener('touchend', function(e) {
      e.stopPropagation();
    });
    
    // Handle touch events for mobile
    const returnAvatar = document.querySelector('.return-avatar');
    if (returnAvatar) {
      returnAvatar.addEventListener('touchend', function(e) {
        e.preventDefault();
        toggleNav(e);
      }, { passive: false });
    }
  }
  
  // Initialize everything when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    initTheme();
    initNavigation();
  });
})();