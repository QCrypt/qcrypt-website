// handling submenus in the navigation
document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.has-children > a');
    
    menuItems.forEach(item => {
      item.addEventListener('click', function(e) {
        if (window.innerWidth < 1200) {  // xl breakpoint
          e.preventDefault();
          const parent = this.parentElement;
          parent.classList.toggle('active');
          
          // Close other open submenus
          menuItems.forEach(other => {
            if (other !== this) {
              other.parentElement.classList.remove('active');
            }
          });
        }
      });
    });
  
    // Close submenus when clicking outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('nav')) {
        menuItems.forEach(item => {
          item.parentElement.classList.remove('active');
        });
      }
    });
  });
