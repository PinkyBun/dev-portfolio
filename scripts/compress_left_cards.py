import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Reduce card subtitle margin
css_content = css_content.replace('margin-bottom: 25px;\n  text-transform: uppercase;', 'margin-bottom: 10px;\n  text-transform: uppercase;')

# Further reduce padding on left cards
css_content = css_content.replace('.experience-card { grid-area: exp; padding: 15px 20px; }', '.experience-card { grid-area: exp; padding: 15px; }')
css_content = css_content.replace('.education-card { grid-area: edu; padding: 15px 20px; }', '.education-card { grid-area: edu; padding: 15px; }')

# Reduce timeline spacing
css_content = css_content.replace('.vertical-timeline {\n  position: relative;\n  padding-left: 20px;\n  margin-top: 10px;\n}', '.vertical-timeline {\n  position: relative;\n  padding-left: 20px;\n  margin-top: 5px;\n}')

# Margin bottom on timeline items
css_content = css_content.replace('margin-bottom: 12px;', 'margin-bottom: 6px;')

# Education item padding
css_content = css_content.replace('padding-bottom: 15px;', 'padding-bottom: 8px;')

# Gap in edu-item
css_content = css_content.replace('.edu-item {\n  display: flex;\n  flex-direction: column;\n  gap: 5px;', '.edu-item {\n  display: flex;\n  flex-direction: column;\n  gap: 2px;')

# Gap in timeline-content
css_content = css_content.replace('.timeline-content {\n  display: flex;\n  flex-direction: column;\n  gap: 5px;', '.timeline-content {\n  display: flex;\n  flex-direction: column;\n  gap: 2px;')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS compression completed.")
