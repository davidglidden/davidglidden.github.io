(function() {
  'use strict';
  
  // Detect if device has touch capability
  function isTouchDevice() {
    return (('ontouchstart' in window) ||
      (navigator.maxTouchPoints > 0) ||
      (navigator.msMaxTouchPoints > 0));
  }
  
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
    if (e) e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  
  // Navigation functionality
  function initNavigation() {
    const quietReturn = document.getElementById('quietReturn');
    const navBloom = document.getElementById('navBloom');
    const returnAvatar = document.querySelector('.return-avatar');
    
    if (!quietReturn || !navBloom || !returnAvatar) return;
    
    // Toggle navigation function
    function toggleNavigation(e) {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      navBloom.classList.toggle('open');
      
      // Toggle body class to prevent scrolling when nav is open
      if (navBloom.classList.contains('open')) {
        document.body.classList.add('nav-open');
      } else {
        document.body.classList.remove('nav-open');
      }
    }
    
    // Show/hide quiet return on scroll
    let ticking = false;
    
    function handleScroll() {
      if (!ticking) {
        window.requestAnimationFrame(function() {
          const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
          
          if (currentScroll > 200) {
            quietReturn.classList.add('visible');
          } else {
            quietReturn.classList.remove('visible');
            navBloom.classList.remove('open');
          }
          
          ticking = false;
        });
        ticking = true;
      }
    }
    
    window.addEventListener('scroll', handleScroll, { passive: true });
    
    // Setup avatar click/touch handling
    if (isTouchDevice()) {
      // For touch devices, handle both touch and click to cover all cases
      let touchHandled = false;
      
      returnAvatar.addEventListener('touchend', function(e) {
        e.preventDefault();
        e.stopPropagation();
        touchHandled = true;
        toggleNavigation();
        
        // Reset flag after a short delay
        setTimeout(function() {
          touchHandled = false;
        }, 300);
      }, { passive: false });
      
      // Fallback click handler for touch devices that don't fire touchend
      returnAvatar.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        if (!touchHandled) {
          toggleNavigation();
        }
      });
    } else {
      // For non-touch devices, just use click
      returnAvatar.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        toggleNavigation();
      });
    }
    
    // Close nav when clicking/touching outside
    function handleOutsideInteraction(e) {
      if (!quietReturn.contains(e.target) && !navBloom.contains(e.target)) {
        navBloom.classList.remove('open');
      }
    }
    
    document.addEventListener('click', handleOutsideInteraction);
    if (isTouchDevice()) {
      document.addEventListener('touchend', handleOutsideInteraction, { passive: true });
    }
    
    // Prevent navigation menu from closing when interacting inside it
    navBloom.addEventListener('click', function(e) {
      e.stopPropagation();
    });
    
    if (isTouchDevice()) {
      navBloom.addEventListener('touchend', function(e) {
        e.stopPropagation();
      }, { passive: true });
    }
    
    // Make the navigation toggle globally accessible
    window.toggleNav = toggleNavigation;
  }
  
  // Initialize everything when DOM is ready
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