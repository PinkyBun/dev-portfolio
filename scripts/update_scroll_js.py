import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '// Tech Stack Filter Logic'
end_marker = '// ==========================================================================\n  // PROJECT DATA REPOSITORY'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''// Tech Stack Filter Logic
  const techFilterBtns = document.querySelectorAll('.tech-filter-btn');
  const techRows = document.querySelectorAll('.tech-category-row');

  if (techFilterBtns.length > 0 && techRows.length > 0) {
    techFilterBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        // Remove active class from all
        techFilterBtns.forEach(b => b.classList.remove('active'));
        // Add active to clicked
        e.target.classList.add('active');
        
        const filterValue = e.target.getAttribute('data-filter');
        
        techRows.forEach(row => {
          const category = row.getAttribute('data-category');
          
          if (filterValue === 'all' || category === filterValue) {
            row.style.display = ''; // Show row
          } else {
            row.style.display = 'none'; // Hide row
          }
        });
      });
    });
  }

  // Tech Stack Horizontal Scroll Buttons Logic
  const scrollBtns = document.querySelectorAll('.tech-scroll-btn');
  scrollBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const isLeft = btn.classList.contains('left');
      const scrollWrapper = btn.closest('.tech-scroll-wrapper');
      const scrollContainer = scrollWrapper.querySelector('.tech-scroll-container');
      
      const scrollAmount = 300; // Pixels to scroll per click
      
      if (scrollContainer) {
        scrollContainer.scrollBy({
          left: isLeft ? -scrollAmount : scrollAmount,
          behavior: 'smooth'
        });
      }
    });
  });

  '''

new_content = content[:start_idx] + replacement + content[end_idx:]

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("JS Replaced successfully")
