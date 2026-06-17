import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Revert HTML
# Find the exact boundaries:
start_marker = '<div class="dashboard-col dashboard-col-left">'
end_marker = '</div>\n          </div>\n        </div>\n      </section>\n\n      <!-- Tech Stack Section -->'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    section = html[start_idx:end_idx]
    
    # Remove wrappers and stats card
    # Instead of complex regex, let's just find and replace the known chunks
    
    # Remove left col wrapper
    html = html.replace('<div class="dashboard-col dashboard-col-left">\n            <!-- Top Left: Experience Card -->', '<!-- Top Left: Experience Card -->')
    
    # Remove right col wrapper and stats card
    stats_chunk = '''</div>
            <div class="dashboard-col dashboard-col-right">
            <!-- Top Right: Stats Card -->
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
    html = html.replace(stats_chunk, '<!-- Top Right: About Text Card -->')
    
    # Restore end tags
    html = html.replace('</div>\n          </div>\n        </div>\n      </section>\n\n      <!-- Tech Stack Section -->', '</div>\n        </div>\n      </section>\n\n      <!-- Tech Stack Section -->')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
else:
    print("HTML Markers not found")

# Revert CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore grid definition
css = css.replace('''.about-dashboard-grid {
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
}''', '''.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  column-gap: 20px;
  row-gap: 15px;
  width: 100%;
}''')

# Restore media query
css = css.replace('''@media (max-width: 992px) {
  .about-dashboard-grid {
    flex-direction: column;
    gap: 15px;
  }
  .dashboard-col-right {
    order: -1; /* Move right col (Stats & About) to top on mobile */
  }
}''', '''@media (max-width: 992px) {
  .about-dashboard-grid {
    grid-template-columns: 1fr;
    grid-template-areas: 
      "about"
      "exp"
      "edu";
    gap: 30px;
  }
}''')

# Restore grid areas
css = css.replace('.experience-card { padding: 12px 15px; }', '.experience-card { grid-area: exp; padding: 12px 15px; }')
css = css.replace('.education-card { padding: 12px 15px; }', '.education-card { grid-area: edu; padding: 12px 15px; }')
css = css.replace('.about-card { }', '.about-card { grid-area: about; align-self: start; }')

# Optionally remove the stats card css if needed, but it won't hurt to leave it.
# Let's remove it to be clean.
start_stat_css = '/* Stats Card */'
end_stat_css = '} /* Ensure we get past the last keyframes */\n'
idx1 = css.find(start_stat_css)
if idx1 != -1:
    idx2 = css.find('}\n', css.find('@keyframes pulse-green')) + 2
    if idx2 != -1:
        css = css[:idx1] + css[idx2:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Reverted stats card and flex layout.")
