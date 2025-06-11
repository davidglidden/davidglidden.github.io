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

// iOS Safari transform bug fix - force cleanup
document.addEventListener('DOMContentLoaded', function() {
  const avatar = document.querySelector('.return-avatar');
  const quietReturn = document.querySelector('.quiet-return');
  const navBloom = document.querySelector('.nav-bloom');
  
  if (/iPhone|iPad|Safari/.test(navigator.userAgent)) {
    console.log('Safari detected - removing all transforms');
    
    if (avatar) {
      avatar.style.transform = 'none';
      avatar.style.webkitTransform = 'none';
    }
    
    if (quietReturn) {
      quietReturn.style.transform = 'none';
      quietReturn.style.webkitTransform = 'none';
    }
    
    if (navBloom) {
      navBloom.style.transform = 'none';
      navBloom.style.webkitTransform = 'none';
    }
    
    console.log('All transforms removed');
  }
});

// iOS Safari compatible mobile fix - NO TRANSFORMS ISSUE RESOLVED
(function() {
  // Only run on actual mobile devices  
  if (/iPhone|Android/i.test(navigator.userAgent) && 'ontouchstart' in window) {
    console.log('Mobile device detected, setting up touch handlers');
    
    function setupMobileNav() {
      const avatar = document.querySelector('.return-avatar');
      if (!avatar) {
        console.log('Avatar not found, retrying...');
        setTimeout(setupMobileNav, 100);
        return;
      }
      
      console.log('Avatar found, setting up touch handling');
      
      // Force remove any CSS that might interfere
      avatar.style.transform = 'none';
      avatar.style.webkitTransform = 'none';
      
      // Ultra-simple touch handler
      avatar.addEventListener('touchstart', function(e) {
        console.log('Touch detected!');
        e.preventDefault();
        
        // Visual feedback
        this.style.opacity = '0.7';
        
        // Direct navigation toggle
        const navBloom = document.getElementById('navBloom');
        if (navBloom) {
          const wasOpen = navBloom.classList.contains('open');
          navBloom.classList.toggle('open');
          console.log('Navigation toggled:', wasOpen ? 'closed' : 'opened');
        }
        
        // Reset opacity
        setTimeout(() => this.style.opacity = '', 200);
        
      }, { passive: false, capture: false });
      
      console.log('Touch handler attached successfully');
    }
    
    // Try immediately, then retry if needed
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', setupMobileNav);
    } else {
      setupMobileNav();
    }
  }
})();

// Fix theme toggle button in menu
document.addEventListener('DOMContentLoaded', function() {
  // Find all theme toggle buttons
  document.querySelectorAll('.theme-toggle-menu').forEach(button => {
    button.removeAttribute('onclick'); // Remove inline handler
    button.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      if (typeof window.toggleTheme === 'function') {
        window.toggleTheme();
      }
    });
  });
});

// Debug mode - add #debug to URL to activate
(function() {
  if (window.location.hash === '#debug') {
    // Create debug panel
    const debugPanel = document.createElement('div');
    debugPanel.id = 'debug-panel';
    debugPanel.style.cssText = `
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(0, 0, 0, 0.9);
      color: #0f0;
      padding: 10px;
      font-family: monospace;
      font-size: 11px;
      max-height: 150px;
      overflow-y: auto;
      z-index: 99999;
      border-top: 2px solid #0f0;
    `;
    debugPanel.innerHTML = '<div style="color: #ff0; margin-bottom: 5px;">DEBUG MODE - Tap avatar to test</div>';
    
    // Add close button
    const closeBtn = document.createElement('button');
    closeBtn.textContent = '✕';
    closeBtn.style.cssText = `
      position: absolute;
      top: 5px;
      right: 5px;
      background: #f00;
      color: #fff;
      border: none;
      padding: 2px 6px;
      cursor: pointer;
      font-size: 12px;
    `;
    closeBtn.onclick = function() {
      debugPanel.remove();
      window.location.hash = '';
    };
    debugPanel.appendChild(closeBtn);
    
    document.body.appendChild(debugPanel);
    
    // Debug log function
    function log(msg, color = '#0f0') {
      const time = new Date().toTimeString().split(' ')[0];
      const line = document.createElement('div');
      line.style.color = color;
      line.textContent = `[${time}] ${msg}`;
      debugPanel.appendChild(line);
      debugPanel.scrollTop = debugPanel.scrollHeight;
    }
    
    // Log basic info
    log('Debug mode active', '#ff0');
    log('User Agent: ' + navigator.userAgent.substring(0, 50) + '...');
    log('Touch support: ' + ('ontouchstart' in window));
    log('Screen: ' + window.innerWidth + 'x' + window.innerHeight);
    
    // Wait for DOM
    document.addEventListener('DOMContentLoaded', function() {
      const avatar = document.querySelector('.return-avatar');
      const navBloom = document.getElementById('navBloom');
      
      log('DOM loaded');
      log('Avatar found: ' + !!avatar, avatar ? '#0f0' : '#f00');
      log('NavBloom found: ' + !!navBloom, navBloom ? '#0f0' : '#f00');
      
      if (avatar) {
        // Check computed styles
        const styles = window.getComputedStyle(avatar);
        log('Avatar z-index: ' + styles.zIndex);
        log('Avatar pointer-events: ' + styles.pointerEvents);
        
        // Monitor ALL events on avatar
        const events = ['click', 'touchstart', 'touchend', 'pointerdown', 'pointerup', 'mousedown', 'mouseup'];
        events.forEach(eventType => {
          avatar.addEventListener(eventType, function(e) {
            log(`Avatar ${eventType.toUpperCase()} fired!`, '#ff0');
            
            // Check if nav opened
            setTimeout(() => {
              if (navBloom && navBloom.classList.contains('open')) {
                log('✓ Nav opened successfully!', '#0f0');
              } else {
                log('✗ Nav did NOT open', '#f00');
              }
            }, 100);
          }, true);
        });
        
        // Check what element is at avatar position
        setTimeout(() => {
          const rect = avatar.getBoundingClientRect();
          const centerX = rect.left + rect.width / 2;
          const centerY = rect.top + rect.height / 2;
          const elementAtPoint = document.elementFromPoint(centerX, centerY);
          
          if (elementAtPoint === avatar) {
            log('✓ Avatar is clickable (no overlap)', '#0f0');
          } else {
            log('✗ Element blocking avatar: ' + (elementAtPoint ? elementAtPoint.className : 'unknown'), '#f00');
          }
        }, 500);
      }
      
      // Monitor toggleNav calls
      const originalToggleNav = window.toggleNav;
      if (originalToggleNav) {
        window.toggleNav = function(e) {
          log('toggleNav() called!', '#ff0');
          return originalToggleNav.call(this, e);
        };
      }
    });
    
    // Log any JavaScript errors
    window.addEventListener('error', function(e) {
      log('ERROR: ' + e.message, '#f00');
    });
  }
})();

// Enhanced debug for blocking element
if (window.location.hash === '#debug2') {
  document.addEventListener('DOMContentLoaded', function() {
    setTimeout(() => {
      const avatar = document.querySelector('.return-avatar');
      if (!avatar) return;
      
      // Get avatar position
      const rect = avatar.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      
      // Find what's at that position
      const blocker = document.elementFromPoint(centerX, centerY);
      
      // Create visual indicator
      const marker = document.createElement('div');
      marker.style.cssText = `
        position: fixed;
        left: ${centerX - 5}px;
        top: ${centerY - 5}px;
        width: 10px;
        height: 10px;
        background: red;
        border: 2px solid yellow;
        border-radius: 50%;
        z-index: 99999;
        pointer-events: none;
      `;
      document.body.appendChild(marker);
      
      // Show detailed info
      alert(`Avatar position: ${Math.round(rect.left)}, ${Math.round(rect.top)}
Avatar size: ${Math.round(rect.width)}x${Math.round(rect.height)}
Element at center: ${blocker ? blocker.tagName + '.' + blocker.className : 'none'}
Parent: ${blocker && blocker.parentElement ? blocker.parentElement.className : 'none'}`);
      
      // Highlight the blocking element
      if (blocker && blocker !== avatar) {
        blocker.style.border = '3px solid red';
        blocker.style.opacity = '0.5';
      }
    }, 1000);
  });
}