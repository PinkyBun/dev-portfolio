import sys

with open('d:/dev-portfolio/js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """      // Meta Row
      const metaCategory = document.getElementById('page-meta-category');
      const metaTools = document.getElementById('page-meta-tools');
      const metaYear = document.getElementById('page-meta-year');
      if (metaCategory) metaCategory.innerText = data.category;
      if (metaTools) metaTools.innerText = data.tags.join(', ');
      if (metaYear) metaYear.innerText = data.year;

      // Overview, Challenge, Approach, Results
      const descOverview = document.getElementById('page-desc-overview');
      const descChallenge = document.getElementById('page-desc-challenge');
      const descApproach = document.getElementById('page-desc-approach');
      const descResults = document.getElementById('page-desc-results');
      if (descOverview) descOverview.innerText = data.overview;
      if (descChallenge) descChallenge.innerText = data.challenge;
      if (descApproach) descApproach.innerText = data.approach;
      if (descResults) descResults.innerText = data.results;

      // Sidebar
      const sideType = document.getElementById('page-side-type');
      const sideTools = document.getElementById('page-side-tools');
      const sideCategory = document.getElementById('page-side-category');
      const sideDuration = document.getElementById('page-side-duration');
      const sideStatus = document.getElementById('page-side-status');
      const liveBtn = document.getElementById('page-live-btn');
      
      if (sideType) sideType.innerText = data.type;
      if (sideTools) sideTools.innerText = data.tags.join(', ');
      if (sideCategory) sideCategory.innerText = data.category;
      if (sideDuration) sideDuration.innerText = data.duration;
      if (sideStatus) sideStatus.innerText = data.status;

      if (liveBtn) {
        if (data.demo) {
          liveBtn.href = data.demo;
          liveBtn.style.display = 'inline-flex';
        } else if (data.github) {
          liveBtn.href = data.github;
          liveBtn.innerHTML = 'View Source Code &rarr;';
          liveBtn.style.display = 'inline-flex';
        } else {
          liveBtn.style.display = 'none';
        }
      }"""

new_block = """      // Icon mapping
      const iconMap = {
        "flutter": "devicon-flutter-plain",
        "dart": "devicon-dart-plain",
        "laravel": "devicon-laravel-original",
        "php": "devicon-php-plain",
        "mysql": "devicon-mysql-plain",
        "sql": "devicon-mysql-plain",
        "bootstrap": "devicon-bootstrap-plain",
        "figma": "devicon-figma-plain",
        "canva": "devicon-canva-original",
        "css grid": "devicon-css3-plain",
      };

      const renderTools = (tags, container) => {
        if (!container) return;
        container.innerHTML = '';
        tags.forEach(tag => {
          const pill = document.createElement('span');
          pill.className = 'tool-pill';
          const lowerTag = tag.toLowerCase();
          let iconClass = iconMap[lowerTag] || 'ti ti-code';
          if (lowerTag.includes('yolo') || lowerTag.includes('resnet') || lowerTag.includes('ml kit')) {
            iconClass = 'ti ti-brain';
          } else if (lowerTag.includes('rfid') || lowerTag.includes('hardware')) {
            iconClass = 'ti ti-cpu';
          } else if (lowerTag.includes('power bi') || lowerTag.includes('excel') || lowerTag.includes('chartjs')) {
            iconClass = 'ti ti-chart-bar';
          } else if (lowerTag.includes('api')) {
            iconClass = 'ti ti-api';
          }
          
          pill.innerHTML = `<i class="${iconClass}"></i> ${tag}`;
          container.appendChild(pill);
        });
      };

      // Meta Row
      const metaCategory = document.getElementById('page-meta-category');
      const metaTools = document.getElementById('page-meta-tools');
      const metaYear = document.getElementById('page-meta-year');
      if (metaCategory) metaCategory.innerText = data.category;
      if (metaTools) renderTools(data.tags, metaTools);
      if (metaYear) metaYear.innerText = data.year;

      // Overview, Challenge, Approach, Results
      const descOverview = document.getElementById('page-desc-overview');
      const descChallenge = document.getElementById('page-desc-challenge');
      const descApproach = document.getElementById('page-desc-approach');
      const descResults = document.getElementById('page-desc-results');
      if (descOverview) descOverview.innerText = data.overview;
      if (descChallenge) descChallenge.innerText = data.challenge;
      if (descApproach) descApproach.innerText = data.approach;
      if (descResults) descResults.innerText = data.results;

      // Sidebar
      const sideType = document.getElementById('page-side-type');
      const sideTools = document.getElementById('page-side-tools');
      const sideCategory = document.getElementById('page-side-category');
      const sideDuration = document.getElementById('page-side-duration');
      const sideStatus = document.getElementById('page-side-status');
      const githubBtn = document.getElementById('page-github-btn');
      const demoBtn = document.getElementById('page-demo-btn');
      
      if (sideType) sideType.innerText = data.type;
      if (sideTools) renderTools(data.tags, sideTools);
      if (sideCategory) sideCategory.innerText = data.category;
      if (sideDuration) sideDuration.innerText = data.duration;
      
      if (sideStatus) {
        const lowerStatus = data.status.toLowerCase();
        let statusClass = 'status-planned';
        if (lowerStatus.includes('complet')) statusClass = 'status-completed';
        else if (lowerStatus.includes('progress') || lowerStatus.includes('active')) statusClass = 'status-active';
        
        sideStatus.innerHTML = `<div class="status-indicator-container ${statusClass}">
          <span class="status-dot"></span>
          <span>${data.status}</span>
        </div>`;
      }

      if (githubBtn) {
        if (data.github) {
          githubBtn.href = data.github;
          githubBtn.style.display = 'inline-flex';
        } else {
          githubBtn.style.display = 'none';
        }
      }

      if (demoBtn) {
        if (data.demo) {
          demoBtn.href = data.demo;
          demoBtn.style.display = 'inline-flex';
        } else {
          demoBtn.style.display = 'none';
        }
      }"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('d:/dev-portfolio/js/main.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated main.js")
else:
    print("Could not find the block in main.js. Let's dump a snippet around it.")
    print(content[content.find("const metaCategory = document.getElementById('page-meta-category');") - 200: content.find("const metaCategory = document.getElementById('page-meta-category');") + 500])
