import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="skills-grouped-container">'
end_marker = '</div>\n        </div>\n      </section>\n\n      <!-- Projects & Experience Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''<div class="bento-grid-container scroll-fade-section">
            
            <!-- JavaScript (FE, Core) -->
            <div class="bento-tile bento-2x2 bento-fe" title="JavaScript">
              <span class="bento-badge">FE</span>
              <div class="tech-icon">
                <i class="devicon-javascript-plain colored"></i>
              </div>
              <span class="tech-label">JavaScript</span>
            </div>

            <!-- Flutter (FE, Core) -->
            <div class="bento-tile bento-2x2 bento-fe" title="Flutter">
              <span class="bento-badge">FE</span>
              <div class="tech-icon">
                <i class="devicon-flutter-plain colored"></i>
              </div>
              <span class="tech-label">Flutter</span>
            </div>

            <!-- Laravel (BE, Core) -->
            <div class="bento-tile bento-2x2 bento-be" title="Laravel">
              <span class="bento-badge">BE</span>
              <div class="tech-icon">
                <i class="devicon-laravel-plain colored"></i>
              </div>
              <span class="tech-label">Laravel</span>
            </div>

            <!-- ChatGPT (AI, Core) -->
            <div class="bento-tile bento-2x2 bento-ai" title="ChatGPT">
              <span class="bento-badge">AI</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/openai.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <span class="tech-label">ChatGPT</span>
            </div>

            <!-- HTML5 (FE, Medium) -->
            <div class="bento-tile bento-2x1 bento-fe" title="HTML5">
              <span class="bento-badge">FE</span>
              <div class="tech-icon">
                <i class="devicon-html5-plain colored"></i>
              </div>
              <span class="tech-label">HTML5</span>
            </div>

            <!-- CSS3 (FE, Medium) -->
            <div class="bento-tile bento-2x1 bento-fe" title="CSS3">
              <span class="bento-badge">FE</span>
              <div class="tech-icon">
                <i class="devicon-css3-plain colored"></i>
              </div>
              <span class="tech-label">CSS3</span>
            </div>

            <!-- PHP (BE, Medium) -->
            <div class="bento-tile bento-2x1 bento-be" title="PHP">
              <span class="bento-badge">BE</span>
              <div class="tech-icon">
                <i class="devicon-php-plain colored"></i>
              </div>
              <span class="tech-label">PHP</span>
            </div>

            <!-- MySQL (DB, Medium) -->
            <div class="bento-tile bento-2x1 bento-db" title="MySQL">
              <span class="bento-badge">DB</span>
              <div class="tech-icon">
                <i class="devicon-mysql-plain colored"></i>
              </div>
              <span class="tech-label">MySQL</span>
            </div>

            <!-- Power BI (DA, Medium) -->
            <div class="bento-tile bento-2x1 bento-da" title="Power BI">
              <span class="bento-badge">DA</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/powerbi.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <span class="tech-label">Power BI</span>
            </div>

            <!-- VS Code (TL, Medium) -->
            <div class="bento-tile bento-2x1 bento-tl" title="VS Code">
              <span class="bento-badge">TL</span>
              <div class="tech-icon">
                <i class="devicon-vscode-plain colored"></i>
              </div>
              <span class="tech-label">VS Code</span>
            </div>

            <!-- GitHub (TL, Medium) -->
            <div class="bento-tile bento-2x1 bento-tl" title="GitHub">
              <span class="bento-badge">TL</span>
              <div class="tech-icon">
                <i class="devicon-github-original colored"></i>
              </div>
              <span class="tech-label">GitHub</span>
            </div>

            <!-- Claude (AI, Medium) -->
            <div class="bento-tile bento-2x1 bento-ai" title="Claude">
              <span class="bento-badge">AI</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/anthropic.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <span class="tech-label">Claude</span>
            </div>

            <!-- 1x1 Tiles Below -->
            <div class="bento-tile bento-1x1 bento-fe" title="Figma">
              <span class="bento-badge">FE</span>
              <div class="tech-icon">
                <i class="devicon-figma-plain colored"></i>
              </div>
              <span class="tech-label">Figma</span>
            </div>

            <div class="bento-tile bento-1x1 bento-fe" title="Canva">
              <span class="bento-badge">FE</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/canva.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <span class="tech-label">Canva</span>
            </div>

            <div class="bento-tile bento-1x1 bento-fe" title="Dart">
              <span class="bento-badge">FE</span>
              <div class="tech-icon">
                <i class="devicon-dart-plain colored"></i>
              </div>
              <span class="tech-label">Dart</span>
            </div>

            <div class="bento-tile bento-1x1 bento-be" title="XAMPP">
              <span class="bento-badge">BE</span>
              <div class="tech-icon">
                <i class="devicon-xampp-plain colored"></i>
              </div>
              <span class="tech-label">XAMPP</span>
            </div>

            <div class="bento-tile bento-1x1 bento-db" title="SQL">
              <span class="bento-badge">DB</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/sqlite.svg" class="si-logo">
              </div>
              <span class="tech-label">SQL</span>
            </div>

            <div class="bento-tile bento-1x1 bento-db" title="Snowflake">
              <span class="bento-badge">DB</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/snowflake.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <span class="tech-label">Snowflake</span>
            </div>

            <div class="bento-tile bento-1x1 bento-da" title="Excel">
              <span class="bento-badge">DA</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftexcel.svg" class="si-logo">
              </div>
              <span class="tech-label">Excel</span>
            </div>

            <div class="bento-tile bento-1x1 bento-tl" title="Git">
              <span class="bento-badge">TL</span>
              <div class="tech-icon">
                <i class="devicon-git-plain colored"></i>
              </div>
              <span class="tech-label">Git</span>
            </div>

            <div class="bento-tile bento-1x1 bento-tl" title="JIRA">
              <span class="bento-badge">TL</span>
              <div class="tech-icon">
                <i class="devicon-jira-plain colored"></i>
              </div>
              <span class="tech-label">JIRA</span>
            </div>

            <div class="bento-tile bento-1x1 bento-tl" title="Google Workspace">
              <span class="bento-badge">TL</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/google.svg" class="si-logo">
              </div>
              <span class="tech-label">Google WS</span>
            </div>

            <div class="bento-tile bento-1x1 bento-tl" title="MS Office">
              <span class="bento-badge">TL</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftoffice.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <span class="tech-label">MS Office</span>
            </div>

            <div class="bento-tile bento-1x1 bento-ai" title="Gemini">
              <span class="bento-badge">AI</span>
              <div class="tech-icon">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/googlegemini.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <span class="tech-label">Gemini</span>
            </div>

            <div class="bento-tile bento-1x1 bento-ai" title="Antigravity">
              <span class="bento-badge">AI</span>
              <div class="tech-icon">
                <i class="ti ti-rocket"></i>
              </div>
              <span class="tech-label">Antigravity</span>
            </div>

          </div>'''

new_content = content[:start_idx] + replacement + '\n' + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced successfully")
