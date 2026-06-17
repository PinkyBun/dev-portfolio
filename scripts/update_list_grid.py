import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- Horizontal Tech Rows -->'
end_marker = '</div>\n        </div>\n      </section>\n\n      <!-- Projects & Experience Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''<!-- 3-Column List Grid -->
          <div class="tech-list-grid collapsed" id="techGrid">
            
            <div class="tech-list-card">
              <div class="tech-card-icon bg-frontend">
                <i class="devicon-javascript-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">JavaScript</h4>
                <p class="tech-card-desc">Dynamic Scripting Language</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-mobile">
                <i class="devicon-flutter-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Flutter</h4>
                <p class="tech-card-desc">Cross-Platform UI Toolkit</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-backend">
                <i class="devicon-laravel-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Laravel</h4>
                <p class="tech-card-desc">PHP Web Framework</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-ai">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/openai.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">ChatGPT</h4>
                <p class="tech-card-desc">Conversational AI Assistant</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-frontend">
                <i class="devicon-html5-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">HTML5</h4>
                <p class="tech-card-desc">Standard Markup Language</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-frontend">
                <i class="devicon-css3-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">CSS3</h4>
                <p class="tech-card-desc">Style Sheet Language</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-backend">
                <i class="devicon-php-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">PHP</h4>
                <p class="tech-card-desc">Server-Side Scripting</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-database">
                <i class="devicon-mysql-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">MySQL</h4>
                <p class="tech-card-desc">Relational Database Management</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-analytics">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/powerbi.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Power BI</h4>
                <p class="tech-card-desc">Business Analytics Service</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-tools">
                <i class="devicon-vscode-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">VS Code</h4>
                <p class="tech-card-desc">Integrated Code Editor</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-tools">
                <i class="devicon-github-original colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">GitHub</h4>
                <p class="tech-card-desc">Version Control Hosting</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-ai">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/anthropic.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Claude</h4>
                <p class="tech-card-desc">Anthropic AI Assistant</p>
              </div>
            </div>
            
            <div class="tech-list-card">
              <div class="tech-card-icon bg-frontend">
                <i class="devicon-figma-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Figma</h4>
                <p class="tech-card-desc">UI/UX Prototyping Tool</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-frontend">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/canva.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Canva</h4>
                <p class="tech-card-desc">Graphic Design Platform</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-mobile">
                <i class="devicon-dart-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Dart</h4>
                <p class="tech-card-desc">Client-Optimized Language</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-backend">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/xampp.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">XAMPP</h4>
                <p class="tech-card-desc">Local Development Environment</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-database">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/sqlite.svg" class="si-logo">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">SQL</h4>
                <p class="tech-card-desc">Structured Query Language</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-database">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/snowflake.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Snowflake</h4>
                <p class="tech-card-desc">Cloud Data Warehouse</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-analytics">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftexcel.svg" class="si-logo">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Excel</h4>
                <p class="tech-card-desc">Spreadsheet Software</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-tools">
                <i class="devicon-git-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Git</h4>
                <p class="tech-card-desc">Version Control System</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-tools">
                <i class="devicon-jira-plain colored"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">JIRA</h4>
                <p class="tech-card-desc">Issue Tracking Software</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-tools">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/google.svg" class="si-logo">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Google Workspace</h4>
                <p class="tech-card-desc">Cloud Productivity Suite</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-tools">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/microsoftoffice.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">MS Office</h4>
                <p class="tech-card-desc">Office Productivity Suite</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-ai">
                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/googlegemini.svg" class="si-logo" style="filter: invert(1);">
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Gemini</h4>
                <p class="tech-card-desc">Google Multimodal AI</p>
              </div>
            </div>

            <div class="tech-list-card">
              <div class="tech-card-icon bg-ai">
                <i class="ti ti-rocket"></i>
              </div>
              <div class="tech-card-content">
                <h4 class="tech-card-title">Antigravity</h4>
                <p class="tech-card-desc">Agentic Coding Assistant</p>
              </div>
            </div>

          </div>
          
          <div class="tech-expand-container">
            <button class="btn btn-outline" id="viewAllTechBtn">View All Technologies</button>
          </div>'''

new_content = content[:start_idx] + replacement + '\n' + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML Replaced successfully")
