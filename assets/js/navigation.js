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
  };

  // Global theme toggle
  window.toggleTheme = function() {
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    
    try {
      localStorage.setItem('theme', newTheme);
    } catch(e) {}
  };

  // Initialize when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);

    // Get elements
    const avatar = document.querySelector('.return-avatar');
    const quietReturn = document.getElementById('quietReturn');
    const navBloom = document.getElementById('navBloom');
    
    if (!avatar || !quietReturn || !navBloom) return;

    // Simple click handler for avatar
    avatar.onclick = function(e) {
      e.preventDefault();
      e.stopPropagation();
      navBloom.classList.toggle('open');
    };
    
    // For iOS - also add touch handler
    avatar.addEventListener('touchend', function(e) {
      e.preventDefault();
      e.stopPropagation();
      navBloom.classList.toggle('open');
    }, { passive: false });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
      if (navBloom.classList.contains('open') && !quietReturn.contains(e.target)) {
        navBloom.classList.remove('open');
      }
    });

    // Scroll visibility
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