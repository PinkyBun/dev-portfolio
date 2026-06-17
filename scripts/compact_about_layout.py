import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make about card height fit content instead of stretching
css_content = css_content.replace('.about-card { grid-area: about; }', '.about-card { grid-area: about; align-self: start; }')

# Reduce padding on left cards
if '.experience-card { grid-area: exp; }' in css_content:
    css_content = css_content.replace('.experience-card { grid-area: exp; }', '.experience-card { grid-area: exp; padding: 15px 20px; }')
if '.education-card { grid-area: edu; }' in css_content:
    css_content = css_content.replace('.education-card { grid-area: edu; }', '.education-card { grid-area: edu; padding: 15px 20px; }')

# Reduce timeline item margin
css_content = css_content.replace('margin-bottom: 20px;', 'margin-bottom: 12px;')

# Reduce vertical timeline gap (if padding or margin was changed)
# we can just find and replace the compact-edu-list gap
css_content = css_content.replace('gap: 15px;', 'gap: 10px;')

# Keep right card padding as is, or reset if needed, but the general dashboard card padding is 20px. 
# Left cards will override with 15px 20px.

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("CSS adjustments for compactness completed.")
