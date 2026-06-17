import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Glassmorphic Container -->'
end_marker = '</div>\n      </section>\n\n      <!-- Tech Stack Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''<!-- Dashboard Grid Container -->
          <div class="about-dashboard-grid">
            
            <!-- Top Left: Experience Card -->
            <div class="dashboard-card experience-card">
              <div class="card-header">
                <div class="header-title-group">
                  <span class="card-dot bg-accent"></span>
                  <h3 class="card-title">Experience</h3>
                </div>
                <div class="stat-box">
                  <span class="stat-number">1+ Years</span>
                  <span class="stat-label">Since 2024</span>
                </div>
              </div>
              <p class="card-subtitle">PROFESSIONAL JOURNEY</p>
              
              <div class="vertical-timeline">
                <div class="timeline-item">
                  <div class="timeline-dot"></div>
                  <div class="timeline-content">
                    <div class="timeline-header">
                      <h4 class="timeline-title">Systems Plus Computer College</h4>
                      <span class="status-pill status-recent">Recent</span>
                    </div>
                    <p class="timeline-desc">BS Information Technology - Graduate</p>
                  </div>
                </div>
                
                <div class="timeline-item">
                  <div class="timeline-dot"></div>
                  <div class="timeline-content">
                    <div class="timeline-header">
                      <h4 class="timeline-title">DOTr — MRT3 Depot Office</h4>
                      <span class="status-pill status-completed">Completed</span>
                    </div>
                    <p class="timeline-desc">OJT / Internship</p>
                  </div>
                </div>

                <div class="timeline-item">
                  <div class="timeline-dot"></div>
                  <div class="timeline-content">
                    <div class="timeline-header">
                      <h4 class="timeline-title">MoneySense Mobile</h4>
                      <span class="status-pill status-completed">Completed</span>
                    </div>
                    <p class="timeline-desc">Capstone Project</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Top Right: About Text Card -->
            <div class="dashboard-card about-card">
              <div class="card-header">
                <div class="header-title-group">
                  <span class="card-dot bg-secondary"></span>
                  <h3 class="card-title">About</h3>
                </div>
              </div>
              <p class="card-subtitle">WHO I AM</p>
              
              <div class="about-text-content">
                <p class="plain-paragraph">
                  I am a fresh graduate in Information Technology from Systems Plus Computer College. Driven by a deep interest in <strong>software engineering</strong> and <strong>application design</strong>, I enjoy creating highly intuitive systems that bridge technical capabilities with functional accessibility.
                </p>
                <p class="plain-paragraph">
                  My background has trained me to approach complex problems systematically and develop <strong>clean, maintainable code</strong>.
                </p>
                <p class="plain-paragraph">
                  My technical skillset spans multiple disciplines, including robust <strong>full-stack web architectures</strong> with <strong>PHP</strong> and <strong>Laravel</strong>. I also specialize in responsive <strong>mobile development</strong> with <strong>Flutter</strong> and <strong>Dart</strong>, alongside database administration using <strong>SQL</strong>.
                </p>
                <p class="plain-paragraph">
                  Additionally, I utilize analytics tools like <strong>Power BI</strong> and Excel to extract and model analytical views from large datasets, enabling <strong>data-centric decision-making</strong>.
                </p>
                <p class="plain-paragraph">
                  I am currently seeking full-time opportunities as an entry-level <strong>Full-Stack Developer</strong>, <strong>Web Developer</strong>, or <strong>Mobile Engineer</strong>. I am excited to contribute to collaborative environments where I can leverage my academic foundation, adapt to <strong>cutting-edge technologies</strong>, and build impactful solutions alongside senior technical professionals.
                </p>
              </div>
            </div>

            <!-- Bottom Left: Education Card -->
            <div class="dashboard-card education-card">
              <div class="card-header">
                <div class="header-title-group">
                  <span class="card-dot bg-primary"></span>
                  <h3 class="card-title">Education</h3>
                </div>
              </div>
              <p class="card-subtitle">ACADEMIC BACKGROUND</p>
              
              <div class="compact-edu-list">
                <div class="edu-item">
                  <div class="edu-row">
                    <span class="edu-school">Systems Plus Computer College</span>
                    <span class="edu-year">2022 - 2026</span>
                  </div>
                  <div class="edu-details">
                    <span>BS Information Technology</span>
                    <span class="edu-divider">•</span>
                    <span>Caloocan City</span>
                  </div>
                </div>

                <div class="edu-item">
                  <div class="edu-row">
                    <span class="edu-school">Arellano University — Elisa Esguerra Campus</span>
                    <span class="edu-year">2020 - 2022</span>
                  </div>
                  <div class="edu-details">
                    <span>STEM</span>
                    <span class="edu-divider">•</span>
                    <span>Malabon City</span>
                    <span class="edu-divider">•</span>
                    <span class="text-highlight">Highest Honors</span>
                  </div>
                </div>
              </div>
            </div>

          </div>'''

new_content = content[:start_idx] + replacement + '\n        ' + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML Replaced successfully")
