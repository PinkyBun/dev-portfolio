import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Reduce container width slightly and padding
css_content = css_content.replace('''.dashboard-container {
  max-width: 1600px !important;
  width: 90% !important;
  margin: 0 auto;
}''', '''.dashboard-container {
  max-width: 1400px !important;
  width: 95% !important;
  margin: 0 auto;
}''')

# Reduce grid gap and column ratio
css_content = css_content.replace('''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 50px;
  width: 100%;
}''', '''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 30px;
  width: 100%;
}''')

# Reduce card padding
css_content = css_content.replace('padding: 40px;', 'padding: 25px;')

# Reduce Timeline margins
css_content = css_content.replace('margin-bottom: 35px;', 'margin-bottom: 20px;')

# Reduce Education list gaps
css_content = css_content.replace('''/* Education spacing */
.compact-edu-list {
  display: flex;
  flex-direction: column;
  gap: 30px; /* Increased gap */
  margin-top: 15px;
}''', '''/* Education spacing */
.compact-edu-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 10px;
}''')

# Reduce About text content gaps
css_content = css_content.replace('''.about-text-content {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.about-text-block {
  display: flex;
  flex-direction: column;
  gap: 10px;
}''', '''.about-text-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.about-text-block {
  display: flex;
  flex-direction: column;
  gap: 4px;
}''')

# Reduce font sizes slightly to help fit
css_content = css_content.replace('font-size: 1.5rem;', 'font-size: 1.3rem;')
css_content = css_content.replace('font-size: 1rem;\n  line-height: 1.7;', 'font-size: 0.9rem;\n  line-height: 1.5;')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Spacing reduced successfully")
