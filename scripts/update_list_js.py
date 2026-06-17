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

replacement = '''// Tech Stack View All Logic
  const viewAllTechBtn = document.getElementById('viewAllTechBtn');
  const techGrid = document.getElementById('techGrid');

  if (viewAllTechBtn && techGrid) {
    viewAllTechBtn.addEventListener('click', () => {
      if (techGrid.classList.contains('collapsed')) {
        // Expand
        techGrid.style.maxHeight = techGrid.scrollHeight + 'px';
        techGrid.classList.remove('collapsed');
        viewAllTechBtn.innerText = 'Show Less';
      } else {
        // Collapse
        techGrid.style.maxHeight = '';
        techGrid.classList.add('collapsed');
        viewAllTechBtn.innerText = 'View All Technologies';
      }
    });
  }

  '''

new_content = content[:start_idx] + replacement + content[end_idx:]

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("JS Replaced successfully")
