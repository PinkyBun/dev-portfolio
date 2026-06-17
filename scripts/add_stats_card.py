import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. Update HTML structure to use columns and insert stats card
stats_card_html = '''<!-- Top Right: Stats Card -->
            <div class="dashboard-card stats-card">
              <div class="about-stats-strip">
                <div class="stat-item" title="Role">
                  <i class="ti ti-code"></i> Full-Stack Developer
                </div>
                <span class="stat-divider">•</span>
                <div class="stat-item" title="Location">
                  <i class="ti ti-map-pin"></i> Malabon City, PH
                </div>
                <span class="stat-divider">•</span>
                <div class="stat-item" title="Education">
                  <i class="ti ti-school"></i> Fresh Graduate
                </div>
                <span class="stat-divider">•</span>
                <div class="stat-item status-active" title="Status">
                  Open to Work
                </div>
                <span class="stat-divider">•</span>
                <div class="stat-item" title="Specialization">
                  <i class="ti ti-layers-intersect"></i> Web & Mobile Dev
                </div>
              </div>
            </div>

            <!-- Top Right: About Text Card -->'''

html_content = html_content.replace('<!-- Top Right: About Text Card -->', stats_card_html)

# Wrap left column
html_content = html_content.replace('<!-- Top Left: Experience Card -->', '<div class="dashboard-col dashboard-col-left">\n            <!-- Top Left: Experience Card -->')
html_content = html_content.replace('<!-- Top Right: Stats Card -->', '</div>\n          <div class="dashboard-col dashboard-col-right">\n            <!-- Top Right: Stats Card -->')
html_content = html_content.replace('</section>\n\n      <!-- Tech Stack Section -->', '</div>\n          </div>\n        </div>\n      </section>\n\n      <!-- Tech Stack Section -->')

# Actually, the last replace might have added an extra </div> because of the grid container.
# Let's do it safely.
# Find the exact boundaries:
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- Dashboard Grid Container -->'
end_marker = '<!-- Tech Stack Section -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    section = html[start_idx:end_idx]
    
    # Inject columns
    section = section.replace('<!-- Top Left: Experience Card -->', '<div class="dashboard-col dashboard-col-left">\n            <!-- Top Left: Experience Card -->')
    section = section.replace('<!-- Top Right: About Text Card -->', '</div>\n            <div class="dashboard-col dashboard-col-right">\n            <!-- Top Right: Stats Card -->\n            <div class="dashboard-card stats-card">\n              <div class="about-stats-strip">\n                <div class="stat-item" title="Role">\n                  <i class="ti ti-code"></i> Full-Stack Developer\n                </div>\n                <span class="stat-divider">•</span>\n                <div class="stat-item" title="Location">\n                  <i class="ti ti-map-pin"></i> Malabon City, PH\n                </div>\n                <span class="stat-divider">•</span>\n                <div class="stat-item" title="Education">\n                  <i class="ti ti-school"></i> Fresh Graduate\n                </div>\n                <span class="stat-divider">•</span>\n                <div class="stat-item status-active" title="Status">\n                  Open to Work\n                </div>\n                <span class="stat-divider">•</span>\n                <div class="stat-item" title="Specialization">\n                  <i class="ti ti-layers-intersect"></i> Web & Mobile Dev\n                </div>\n              </div>\n            </div>\n\n            <!-- Top Right: About Text Card -->')
    
    # Close the right col before the end of the grid container
    # The grid container ends right before `</div>\n        </div>\n      </section>`
    section = section.replace('</div>\n        </div>\n      </section>', '</div>\n          </div>\n        </div>\n      </section>')
    
    html = html[:start_idx] + section + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
else:
    print("HTML Markers not found")

# 2. Update CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace grid areas with flex
css = css.replace('''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  column-gap: 20px;
  row-gap: 15px;
  width: 100%;
}''', '''.about-dashboard-grid {
  display: flex;
  gap: 20px;
  width: 100%;
}
.dashboard-col {
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.dashboard-col-left {
  flex: 1;
}
.dashboard-col-right {
  flex: 1.4;
}''')

css = css.replace('''@media (max-width: 992px) {
  .about-dashboard-grid {
    grid-template-columns: 1fr;
    grid-template-areas: 
      "about"
      "exp"
      "edu";
    gap: 30px;
  }
}''', '''@media (max-width: 992px) {
  .about-dashboard-grid {
    flex-direction: column;
    gap: 15px;
  }
  .dashboard-col-right {
    order: -1; /* Move right col (Stats & About) to top on mobile */
  }
}''')

# Add stat strip CSS if it was removed
stat_strip_css = '''
/* Stats Card */
.stats-card {
  padding: 15px 20px;
}

.about-stats-strip {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 12px;
  font-family: var(--font-monospace);
  font-size: 12px;
  color: var(--text-secondary);
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 6px;
}

.stat-item i {
  font-size: 1.1rem;
  color: var(--accent);
}

.stat-divider {
  color: rgba(167, 139, 250, 0.3);
  font-size: 10px;
}

.status-active {
  color: #4ade80 !important;
}
.status-active::after {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: #4ade80;
  display: inline-block;
  box-shadow: 0 0 8px #4ade80;
  animation: pulse-green 1.5s infinite alternate;
}
@keyframes pulse-green {
  from { transform: scale(0.9); opacity: 0.6; box-shadow: 0 0 4px #4ade80; }
  to { transform: scale(1.2); opacity: 1; box-shadow: 0 0 10px #4ade80; }
}
'''
if '.about-stats-strip' not in css:
    css += stat_strip_css

# We don't need grid-area definitions anymore but they don't hurt.
css = css.replace('.experience-card { grid-area: exp; padding: 12px 15px; }', '.experience-card { padding: 12px 15px; }')
css = css.replace('.education-card { grid-area: edu; padding: 12px 15px; }', '.education-card { padding: 12px 15px; }')
css = css.replace('.about-card { grid-area: about; align-self: start; }', '.about-card { }')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added stats card and switched to flex columns.")
