import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Adjust container max-width to make the whole thing less wide (avoid too many spaces)
css_content = css_content.replace('''.dashboard-container {
  max-width: 1400px !important;
  width: 95% !important;
  margin: 0 auto;
}''', '''.dashboard-container {
  max-width: 1150px !important;
  width: 95% !important;
  margin: 0 auto;
}''')

# Adjust grid-template-columns to make left cards smaller and right card wider, and reduce gap
css_content = css_content.replace('''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 30px;
  width: 100%;
}''', '''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 20px;
  width: 100%;
}''')

# Also let's reduce the padding a bit more to avoid empty spaces inside the cards
css_content = css_content.replace('padding: 25px;', 'padding: 20px;')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Grid adjusted successfully")
