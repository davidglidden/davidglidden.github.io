// Theme toggle with persistence
function toggleTheme() {
  const currentTheme = document.body.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.body.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

// Load saved theme
document.addEventListener('DOMContentLoaded', function() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.body.setAttribute('data-theme', savedTheme);
  
  // Quiet return visibility
  const quietReturn = document.getElementById('quietReturn');
  const navBloom = document.getElementById('navBloom');
  
  if (quietReturn) {
    window.addEventListener('scroll', () => {
      const scrollPercent = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
      
      if (scrollPercent > 0.3) {
        quietReturn.classList.add('visible');
      } else {
        quietReturn.classList.remove('visible');
        navBloom.classList.remove('open');
      }
    });
  }
});

// Toggle navigation bloom
function toggleNav() {
  const navBloom = document.getElementById('navBloom');
  navBloom.classList.toggle('open');
}

// Close nav when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('.quiet-return')) {
    const navBloom = document.getElementById('navBloom');
    if (navBloom) {
      navBloom.classList.remove('open');
    }
  }
});

// Smooth scroll to top
function scrollToTop(e) {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: 'smooth' });
  const navBloom = document.getElementById('navBloom');
  navBloom.classList.remove('open');
}