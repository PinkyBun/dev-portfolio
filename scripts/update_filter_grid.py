import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="bento-grid-container scroll-fade-section">'
end_marker = '<!-- Projects & Experience Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

# Note: The end_marker is actually after the closing tags of the section, so we should back up a bit.
# Let's just find '</div>\n        </div>\n      </section>\n\n      <!-- Projects & Experience Section -->'
end_marker_actual = '</div>\n        </div>\n      </section>\n\n      <!-- Projects & Experience Section -->'
end_idx_actual = content.find(end_marker_actual)

replacement = '''<!-- Tech Filter Bar -->
          <div class="tech-filter-container scroll-fade-section">
            <button class="tech-filter-btn active" data-filter="all">All</button>
            <button class="tech-filter-btn" data-filter="frontend">Frontend</button>
            <button class="tech-filter-btn" data-filter="backend">Backend</button>
            <button class="tech-filter-btn" data-filter="mobile">Mobile</button>
            <button class="tech-filter-btn" data-filter="database">Database</button>
            <button class="tech-filter-btn" data-filter="data-analytics">Data & Analytics</button>
            <button class="tech-filter-btn" data-filter="tools">Tools</button>
            <button class="tech-filter-btn" data-filter="ai">AI Tools</button>
          </div>
          
          <!-- Filterable Tech Grid -->
          <div class="tech-grid-filterable scroll-fade-section" id="tech-grid">
            
            <!-- Frontend -->
            <div class="tech-card border-frontend" data-category="frontend" title="JavaScript">
              <div class="tech-icon"><i class="devicon-javascript-plain colored"></i></div>
              <span class="tech-label">JavaScript</span>
            </div>
            <div class="tech-card border-frontend" data-category="frontend" title="HTML5">
              <div class="tech-icon"><i class="devicon-html5-plain colored"></i></div>
              <span class="tech-label">HTML5</span>
            </div>
            <div class="tech-card border-frontend" data-category="frontend" title="CSS3">
              <div class="tech-icon"><i class="devicon-css3-plain colored"></i></div>
              <span class="tech-label">CSS3</span>
            </div>
            <div class="tech-card border-frontend" data-category="frontend" title="Figma">
              <div class="tech-icon"><i class="devicon-figma-plain colored"></i></div>
              <span class="tech-label">Figma</span>
            </div>
            <div class="tech-card border-frontend" data-category="frontend" title="Canva">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/canva.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">Canva</span>
            </div>

            <!-- Mobile -->
            <div class="tech-card border-mobile" data-category="mobile" title="Flutter">
              <div class="tech-icon"><i class="devicon-flutter-plain colored"></i></div>
              <span class="tech-label">Flutter</span>
            </div>
            <div class="tech-card border-mobile" data-category="mobile" title="Dart">
              <div class="tech-icon"><i class="devicon-dart-plain colored"></i></div>
              <span class="tech-label">Dart</span>
            </div>

            <!-- Backend -->
            <div class="tech-card border-backend" data-category="backend" title="Laravel">
              <div class="tech-icon"><i class="devicon-laravel-plain colored"></i></div>
              <span class="tech-label">Laravel</span>
            </div>
            <div class="tech-card border-backend" data-category="backend" title="PHP">
              <div class="tech-icon"><i class="devicon-php-plain colored"></i></div>
              <span class="tech-label">PHP</span>
            </div>
            <div class="tech-card border-backend" data-category="backend" title="XAMPP">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/xampp.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">XAMPP</span>
            </div>

            <!-- Database -->
            <div class="tech-card border-database" data-category="database" title="MySQL">
              <div class="tech-icon"><i class="devicon-mysql-plain colored"></i></div>
              <span class="tech-label">MySQL</span>
            </div>
            <div class="tech-card border-database" data-category="database" title="SQL">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/sqlite.svg" class="si-logo"></div>
              <span class="tech-label">SQL</span>
            </div>
            <div class="tech-card border-database" data-category="database" title="Snowflake">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/snowflake.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">Snowflake</span>
            </div>

            <!-- Data & Analytics -->
            <div class="tech-card border-analytics" data-category="data-analytics" title="Power BI">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/powerbi.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">Power BI</span>
            </div>
            <div class="tech-card border-analytics" data-category="data-analytics" title="Excel">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftexcel.svg" class="si-logo"></div>
              <span class="tech-label">Excel</span>
            </div>

            <!-- Tools -->
            <div class="tech-card border-tools" data-category="tools" title="VS Code">
              <div class="tech-icon"><i class="devicon-vscode-plain colored"></i></div>
              <span class="tech-label">VS Code</span>
            </div>
            <div class="tech-card border-tools" data-category="tools" title="GitHub">
              <div class="tech-icon"><i class="devicon-github-original colored"></i></div>
              <span class="tech-label">GitHub</span>
            </div>
            <div class="tech-card border-tools" data-category="tools" title="Git">
              <div class="tech-icon"><i class="devicon-git-plain colored"></i></div>
              <span class="tech-label">Git</span>
            </div>
            <div class="tech-card border-tools" data-category="tools" title="JIRA">
              <div class="tech-icon"><i class="devicon-jira-plain colored"></i></div>
              <span class="tech-label">JIRA</span>
            </div>
            <div class="tech-card border-tools" data-category="tools" title="Google Workspace">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/google.svg" class="si-logo"></div>
              <span class="tech-label">Google WS</span>
            </div>
            <div class="tech-card border-tools" data-category="tools" title="MS Office">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftoffice.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">MS Office</span>
            </div>

            <!-- AI Tools -->
            <div class="tech-card border-ai" data-category="ai" title="ChatGPT">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/openai.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">ChatGPT</span>
            </div>
            <div class="tech-card border-ai" data-category="ai" title="Claude">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/anthropic.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">Claude</span>
            </div>
            <div class="tech-card border-ai" data-category="ai" title="Gemini">
              <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/googlegemini.svg" class="si-logo" style="filter: invert(1);"></div>
              <span class="tech-label">Gemini</span>
            </div>
            <div class="tech-card border-ai" data-category="ai" title="Antigravity">
              <div class="tech-icon"><i class="ti ti-rocket"></i></div>
              <span class="tech-label">Antigravity</span>
            </div>

          </div>'''

new_content = content[:start_idx] + replacement + '\n' + content[end_idx_actual:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML Replaced successfully")
