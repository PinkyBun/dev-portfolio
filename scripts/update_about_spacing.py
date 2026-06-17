import re

# Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change container to container-fluid for About section
content = content.replace('<section id="about" class="about-section section-bg-2 scroll-fade">\n        <div class="container">',
                          '<section id="about" class="about-section section-bg-2 scroll-fade">\n        <div class="container-fluid dashboard-container">')

# Restore the section headers
about_card_start = '<!-- Top Right: About Text Card -->'
about_card_end = '<!-- Bottom Left: Education Card -->'
start_idx = content.find(about_card_start)
end_idx = content.find(about_card_end)

new_about_card = '''<!-- Top Right: About Text Card -->
            <div class="dashboard-card about-card">
              <div class="card-header">
                <div class="header-title-group">
                  <span class="card-dot bg-secondary"></span>
                  <h3 class="card-title">About</h3>
                </div>
              </div>
              <p class="card-subtitle">WHO I AM</p>
              
              <div class="about-text-content">
                <div class="about-text-block">
                  <h3 class="about-prompt monospace">&gt; WHO I AM</h3>
                  <p class="plain-paragraph">
                    I am a fresh graduate in Information Technology from Systems Plus Computer College. Driven by a deep interest in <strong>software engineering</strong> and <strong>application design</strong>, I enjoy creating highly intuitive systems that bridge technical capabilities with functional accessibility.
                  </p>
                  <p class="plain-paragraph">
                    My background has trained me to approach complex problems systematically and develop <strong>clean, maintainable code</strong>.
                  </p>
                </div>
                
                <div class="about-text-block">
                  <h3 class="about-prompt monospace">&gt; WHAT I CAN DO</h3>
                  <p class="plain-paragraph">
                    My technical skillset spans multiple disciplines, including robust <strong>full-stack web architectures</strong> with <strong>PHP</strong> and <strong>Laravel</strong>. I also specialize in responsive <strong>mobile development</strong> with <strong>Flutter</strong> and <strong>Dart</strong>, alongside database administration using <strong>SQL</strong>.
                  </p>
                  <p class="plain-paragraph">
                    Additionally, I utilize analytics tools like <strong>Power BI</strong> and Excel to extract and model analytical views from large datasets, enabling <strong>data-centric decision-making</strong>.
                  </p>
                </div>
                
                <div class="about-text-block">
                  <h3 class="about-prompt monospace">&gt; WHAT I'M LOOKING FOR</h3>
                  <p class="plain-paragraph">
                    I am currently seeking full-time opportunities as an entry-level <strong>Full-Stack Developer</strong>, <strong>Web Developer</strong>, or <strong>Mobile Engineer</strong>.
                  </p>
                  <p class="plain-paragraph">
                    I am excited to contribute to collaborative environments where I can leverage my academic foundation, adapt to <strong>cutting-edge technologies</strong>, and build impactful solutions alongside senior technical professionals.
                  </p>
                </div>
              </div>
            </div>

            '''

content = content[:start_idx] + new_about_card + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

css_replacement = '''
/* Dashboard Container */
.dashboard-container {
  max-width: 1600px; /* Much wider for dashboard feel */
  padding-left: 5%;
  padding-right: 5%;
}

.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 50px; /* Increased gap */
  width: 100%;
}

@media (max-width: 992px) {
  .about-dashboard-grid {
    grid-template-columns: 1fr;
    grid-template-areas: 
      "about"
      "exp"
      "edu";
    gap: 30px;
  }
}

.dashboard-card {
  background-color: var(--bg-tertiary);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 40px; /* Increased padding */
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Timeline updates for spacing */
.timeline-item {
  position: relative;
  margin-bottom: 35px; /* Increased bottom margin */
}

/* Education spacing */
.compact-edu-list {
  display: flex;
  flex-direction: column;
  gap: 30px; /* Increased gap */
  margin-top: 15px;
}

/* About Text Blocks */
.about-text-content {
  display: flex;
  flex-direction: column;
  gap: 30px; /* Increased gap between sections */
}

.about-text-block {
  display: flex;
  flex-direction: column;
  gap: 12px; /* Gap between header and paragraphs */
}

.about-prompt {
  font-family: var(--font-monospace);
  color: #a78bfa;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.05em;
  margin: 0;
  margin-bottom: 5px;
}

[data-theme="light"] .about-prompt {
  color: #7c3aed;
}

'''

# We need to replace the grid layout and padding in css
# I will just append the specific overrides or replace them precisely.
# Let's replace precisely
css_content = css_content.replace('''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 24px;
  width: 100%;
}''', '''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 50px;
  width: 100%;
}''')

css_content = css_content.replace('padding: 30px;', 'padding: 40px;')
css_content = css_content.replace('margin-bottom: 25px;', 'margin-bottom: 35px;')
css_content = css_content.replace('gap: 20px;', 'gap: 30px;')

# For .about-text-content
css_content = css_content.replace('''.about-text-content {
  display: flex;
  flex-direction: column;
  gap: 18px;
}''', '''.about-text-content {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.about-text-block {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.about-prompt {
  font-family: var(--font-monospace);
  color: #a78bfa;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.05em;
  margin: 0 0 5px 0;
}
[data-theme="light"] .about-prompt {
  color: #7c3aed;
}
''')

# Add dashboard-container definition near the top of the file or at the end
css_content += '''
.dashboard-container {
  max-width: 1600px !important;
  width: 90% !important;
  margin: 0 auto;
}
'''

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Update completed")
