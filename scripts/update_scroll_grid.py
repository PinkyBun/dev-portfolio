import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Filterable Tech Grid -->'
end_marker = '</div>\n        </div>\n      </section>\n\n      <!-- Projects & Experience Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''<!-- Horizontal Tech Rows -->
          <div id="tech-rows-container">
            
            <!-- Frontend -->
            <div class="tech-category-row scroll-fade-section" data-category="frontend">
              <h3 class="tech-row-title monospace">FRONTEND &rarr;</h3>
              <div class="tech-scroll-wrapper">
                <div class="scroll-fade-gradient left"></div>
                <button class="tech-scroll-btn left" aria-label="Scroll left"><i class="ti ti-chevron-left"></i></button>
                <div class="tech-scroll-container">
                  <div class="tech-card border-frontend" title="JavaScript">
                    <div class="tech-icon"><i class="devicon-javascript-plain colored"></i></div>
                    <span class="tech-label">JavaScript</span>
                  </div>
                  <div class="tech-card border-frontend" title="HTML5">
                    <div class="tech-icon"><i class="devicon-html5-plain colored"></i></div>
                    <span class="tech-label">HTML5</span>
                  </div>
                  <div class="tech-card border-frontend" title="CSS3">
                    <div class="tech-icon"><i class="devicon-css3-plain colored"></i></div>
                    <span class="tech-label">CSS3</span>
                  </div>
                  <div class="tech-card border-frontend" title="Figma">
                    <div class="tech-icon"><i class="devicon-figma-plain colored"></i></div>
                    <span class="tech-label">Figma</span>
                  </div>
                  <div class="tech-card border-frontend" title="Canva">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/canva.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">Canva</span>
                  </div>
                </div>
                <button class="tech-scroll-btn right" aria-label="Scroll right"><i class="ti ti-chevron-right"></i></button>
                <div class="scroll-fade-gradient right"></div>
              </div>
            </div>

            <!-- Mobile -->
            <div class="tech-category-row scroll-fade-section" data-category="mobile">
              <h3 class="tech-row-title monospace">MOBILE &rarr;</h3>
              <div class="tech-scroll-wrapper">
                <div class="scroll-fade-gradient left"></div>
                <button class="tech-scroll-btn left" aria-label="Scroll left"><i class="ti ti-chevron-left"></i></button>
                <div class="tech-scroll-container">
                  <div class="tech-card border-mobile" title="Flutter">
                    <div class="tech-icon"><i class="devicon-flutter-plain colored"></i></div>
                    <span class="tech-label">Flutter</span>
                  </div>
                  <div class="tech-card border-mobile" title="Dart">
                    <div class="tech-icon"><i class="devicon-dart-plain colored"></i></div>
                    <span class="tech-label">Dart</span>
                  </div>
                </div>
                <button class="tech-scroll-btn right" aria-label="Scroll right"><i class="ti ti-chevron-right"></i></button>
                <div class="scroll-fade-gradient right"></div>
              </div>
            </div>

            <!-- Backend -->
            <div class="tech-category-row scroll-fade-section" data-category="backend">
              <h3 class="tech-row-title monospace">BACKEND &rarr;</h3>
              <div class="tech-scroll-wrapper">
                <div class="scroll-fade-gradient left"></div>
                <button class="tech-scroll-btn left" aria-label="Scroll left"><i class="ti ti-chevron-left"></i></button>
                <div class="tech-scroll-container">
                  <div class="tech-card border-backend" title="Laravel">
                    <div class="tech-icon"><i class="devicon-laravel-plain colored"></i></div>
                    <span class="tech-label">Laravel</span>
                  </div>
                  <div class="tech-card border-backend" title="PHP">
                    <div class="tech-icon"><i class="devicon-php-plain colored"></i></div>
                    <span class="tech-label">PHP</span>
                  </div>
                  <div class="tech-card border-backend" title="XAMPP">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/xampp.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">XAMPP</span>
                  </div>
                </div>
                <button class="tech-scroll-btn right" aria-label="Scroll right"><i class="ti ti-chevron-right"></i></button>
                <div class="scroll-fade-gradient right"></div>
              </div>
            </div>

            <!-- Database -->
            <div class="tech-category-row scroll-fade-section" data-category="database">
              <h3 class="tech-row-title monospace">DATABASE &rarr;</h3>
              <div class="tech-scroll-wrapper">
                <div class="scroll-fade-gradient left"></div>
                <button class="tech-scroll-btn left" aria-label="Scroll left"><i class="ti ti-chevron-left"></i></button>
                <div class="tech-scroll-container">
                  <div class="tech-card border-database" title="MySQL">
                    <div class="tech-icon"><i class="devicon-mysql-plain colored"></i></div>
                    <span class="tech-label">MySQL</span>
                  </div>
                  <div class="tech-card border-database" title="SQL">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/sqlite.svg" class="si-logo"></div>
                    <span class="tech-label">SQL</span>
                  </div>
                  <div class="tech-card border-database" title="Snowflake">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/snowflake.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">Snowflake</span>
                  </div>
                </div>
                <button class="tech-scroll-btn right" aria-label="Scroll right"><i class="ti ti-chevron-right"></i></button>
                <div class="scroll-fade-gradient right"></div>
              </div>
            </div>

            <!-- Data & Analytics -->
            <div class="tech-category-row scroll-fade-section" data-category="data-analytics">
              <h3 class="tech-row-title monospace">DATA & ANALYTICS &rarr;</h3>
              <div class="tech-scroll-wrapper">
                <div class="scroll-fade-gradient left"></div>
                <button class="tech-scroll-btn left" aria-label="Scroll left"><i class="ti ti-chevron-left"></i></button>
                <div class="tech-scroll-container">
                  <div class="tech-card border-analytics" title="Power BI">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/powerbi.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">Power BI</span>
                  </div>
                  <div class="tech-card border-analytics" title="Excel">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftexcel.svg" class="si-logo"></div>
                    <span class="tech-label">Excel</span>
                  </div>
                </div>
                <button class="tech-scroll-btn right" aria-label="Scroll right"><i class="ti ti-chevron-right"></i></button>
                <div class="scroll-fade-gradient right"></div>
              </div>
            </div>

            <!-- Tools -->
            <div class="tech-category-row scroll-fade-section" data-category="tools">
              <h3 class="tech-row-title monospace">TOOLS &rarr;</h3>
              <div class="tech-scroll-wrapper">
                <div class="scroll-fade-gradient left"></div>
                <button class="tech-scroll-btn left" aria-label="Scroll left"><i class="ti ti-chevron-left"></i></button>
                <div class="tech-scroll-container">
                  <div class="tech-card border-tools" title="VS Code">
                    <div class="tech-icon"><i class="devicon-vscode-plain colored"></i></div>
                    <span class="tech-label">VS Code</span>
                  </div>
                  <div class="tech-card border-tools" title="GitHub">
                    <div class="tech-icon"><i class="devicon-github-original colored"></i></div>
                    <span class="tech-label">GitHub</span>
                  </div>
                  <div class="tech-card border-tools" title="Git">
                    <div class="tech-icon"><i class="devicon-git-plain colored"></i></div>
                    <span class="tech-label">Git</span>
                  </div>
                  <div class="tech-card border-tools" title="JIRA">
                    <div class="tech-icon"><i class="devicon-jira-plain colored"></i></div>
                    <span class="tech-label">JIRA</span>
                  </div>
                  <div class="tech-card border-tools" title="Google Workspace">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/google.svg" class="si-logo"></div>
                    <span class="tech-label">Google WS</span>
                  </div>
                  <div class="tech-card border-tools" title="MS Office">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftoffice.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">MS Office</span>
                  </div>
                </div>
                <button class="tech-scroll-btn right" aria-label="Scroll right"><i class="ti ti-chevron-right"></i></button>
                <div class="scroll-fade-gradient right"></div>
              </div>
            </div>

            <!-- AI Tools -->
            <div class="tech-category-row scroll-fade-section" data-category="ai">
              <h3 class="tech-row-title monospace">AI TOOLS &rarr;</h3>
              <div class="tech-scroll-wrapper">
                <div class="scroll-fade-gradient left"></div>
                <button class="tech-scroll-btn left" aria-label="Scroll left"><i class="ti ti-chevron-left"></i></button>
                <div class="tech-scroll-container">
                  <div class="tech-card border-ai" title="ChatGPT">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/openai.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">ChatGPT</span>
                  </div>
                  <div class="tech-card border-ai" title="Claude">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/anthropic.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">Claude</span>
                  </div>
                  <div class="tech-card border-ai" title="Gemini">
                    <div class="tech-icon"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/googlegemini.svg" class="si-logo" style="filter: invert(1);"></div>
                    <span class="tech-label">Gemini</span>
                  </div>
                  <div class="tech-card border-ai" title="Antigravity">
                    <div class="tech-icon"><i class="ti ti-rocket"></i></div>
                    <span class="tech-label">Antigravity</span>
                  </div>
                </div>
                <button class="tech-scroll-btn right" aria-label="Scroll right"><i class="ti ti-chevron-right"></i></button>
                <div class="scroll-fade-gradient right"></div>
              </div>
            </div>

          </div>'''

new_content = content[:start_idx] + replacement + '\n' + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML Replaced successfully")
