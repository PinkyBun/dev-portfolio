import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Font sizes
css_content = css_content.replace('font-size: 1.3rem;', 'font-size: 1.1rem;')
css_content = css_content.replace('font-size: 0.75rem;', 'font-size: 0.65rem;')

# Timeline title and description
css_content = css_content.replace('.timeline-title {\n  font-size: 1rem;', '.timeline-title {\n  font-size: 0.85rem;')
css_content = css_content.replace('.timeline-desc {\n  font-size: 0.9rem;', '.timeline-desc {\n  font-size: 0.8rem;')

# Education school and details
css_content = css_content.replace('.edu-school {\n  font-size: 1rem;', '.edu-school {\n  font-size: 0.85rem;')
css_content = css_content.replace('.edu-details {\n  display: flex;\n  align-items: center;\n  flex-wrap: wrap;\n  gap: 8px;\n  font-size: 0.9rem;', '.edu-details {\n  display: flex;\n  align-items: center;\n  flex-wrap: wrap;\n  gap: 8px;\n  font-size: 0.8rem;')
css_content = css_content.replace('.edu-year {\n  font-size: 0.85rem;', '.edu-year {\n  font-size: 0.75rem;')

# Stat box
css_content = css_content.replace('.stat-number {\n  font-size: 1.1rem;', '.stat-number {\n  font-size: 0.9rem;')
css_content = css_content.replace('.stat-label {\n  font-size: 0.7rem;', '.stat-label {\n  font-size: 0.6rem;')

# Pills
css_content = css_content.replace('.status-pill {\n  font-size: 0.7rem;', '.status-pill {\n  font-size: 0.6rem;\n  padding: 2px 6px;')

# Padding
css_content = css_content.replace('.experience-card { grid-area: exp; padding: 15px; }', '.experience-card { grid-area: exp; padding: 12px 15px; }')
css_content = css_content.replace('.education-card { grid-area: edu; padding: 15px; }', '.education-card { grid-area: edu; padding: 12px 15px; }')

# Subtitle margin
css_content = css_content.replace('margin-bottom: 10px;\n  text-transform: uppercase;', 'margin-bottom: 5px;\n  text-transform: uppercase;')

# Timeline item margin
css_content = css_content.replace('margin-bottom: 6px;', 'margin-bottom: 4px;')

# Gaps
css_content = css_content.replace('.edu-item {\n  display: flex;\n  flex-direction: column;\n  gap: 2px;\n  padding-bottom: 8px;', '.edu-item {\n  display: flex;\n  flex-direction: column;\n  gap: 0px;\n  padding-bottom: 5px;')
css_content = css_content.replace('.timeline-content {\n  display: flex;\n  flex-direction: column;\n  gap: 2px;', '.timeline-content {\n  display: flex;\n  flex-direction: column;\n  gap: 0px;')

# Row gap vs column gap in dashboard grid
css_content = css_content.replace('gap: 20px;\n  width: 100%;', 'column-gap: 20px;\n  row-gap: 15px;\n  width: 100%;')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS font sizes and spacing reduced successfully.")
