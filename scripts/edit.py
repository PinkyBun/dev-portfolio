import sys

with open('d:/dev-portfolio/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = """  // ==========================================================================
  // DYNAMIC PROJECT PAGE POPULATION
  // ==========================================================================
  // Check if we are on the project.html page
  if (window.location.pathname.includes('project.html')) {
    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get('id');
    const data = projectData[projectId];

    if (data) {
      // Document Title
      document.title = `${data.title} | Jasmine A. Nalda`;

      // Breadcrumb & Title
      const breadcrumbTitle = document.getElementById('page-breadcrumb-title');
      const mainTitle = document.getElementById('page-main-title');
      if (breadcrumbTitle) breadcrumbTitle.innerText = data.title;
      if (mainTitle) mainTitle.innerText = data.title;

      // Meta Row
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
      }

      // Slider Logic
      const slidesWrapper = document.getElementById('page-slider-wrapper');
      const prevBtn = document.getElementById('page-slider-prev');
      const nextBtn = document.getElementById('page-slider-next');
      const dotsContainer = document.getElementById('page-slider-indicators');
      
      let currentSlideIndex = 0;
      let totalSlidesCount = data.images.length;

      if (slidesWrapper) {
        slidesWrapper.innerHTML = '';
        data.images.forEach(imgSrc => {
          const img = document.createElement('img');
          img.src = imgSrc;
          img.alt = `${data.title} View`;
          img.className = 'slide-img';
          img.onerror = () => {
            const errorFallback = document.createElement('div');
            errorFallback.style.width = '100%';
            errorFallback.style.height = '100%';
            errorFallback.style.display = 'flex';
            errorFallback.style.alignItems = 'center';
            errorFallback.style.justifyContent = 'center';
            errorFallback.style.backgroundColor = '#19162c';
            errorFallback.style.color = '#a78bfa';
            errorFallback.style.fontFamily = 'var(--font-monospace)';
            errorFallback.innerText = `[ IMAGE WORKPLACE: ${imgSrc} ]`;
            img.replaceWith(errorFallback);
          };
          slidesWrapper.appendChild(img);
        });

        if (dotsContainer) {
          dotsContainer.innerHTML = '';
          for (let i = 0; i < totalSlidesCount; i++) {
            const dot = document.createElement('div');
            dot.className = `dot ${i === 0 ? 'active' : ''}`;
            dot.addEventListener('click', () => navigateToSlide(i));
            dotsContainer.appendChild(dot);
          }
        }

        function navigateToSlide(index) {
          if (index < 0) {
            currentSlideIndex = totalSlidesCount - 1;
          } else if (index >= totalSlidesCount) {
            currentSlideIndex = 0;
          } else {
            currentSlideIndex = index;
          }
          updateSliderPosition();
        }

        function updateSliderPosition() {
          slidesWrapper.style.transform = `translateX(-${currentSlideIndex * 100}%)`;
          if (dotsContainer) {
            const dots = dotsContainer.querySelectorAll('.dot');
            dots.forEach((dot, idx) => {
              if (idx === currentSlideIndex) {
                dot.classList.add('active');
              } else {
                dot.classList.remove('active');
              }
            });
          }
        }

        if (prevBtn) prevBtn.addEventListener('click', () => navigateToSlide(currentSlideIndex - 1));
        if (nextBtn) nextBtn.addEventListener('click', () => navigateToSlide(currentSlideIndex + 1));
      }
      
      // Next Project Logic
      const keys = Object.keys(projectData);
      const currentIndex = keys.indexOf(projectId);
      if (currentIndex !== -1) {
        const nextIndex = (currentIndex + 1) % keys.length;
        const nextId = keys[nextIndex];
        const nextProject = projectData[nextId];
        
        const nextLinkTitle = document.getElementById('page-next-link');
        const nextBtnLink = document.getElementById('page-next-btn');
        
        if (nextLinkTitle) {
          nextLinkTitle.innerText = nextProject.title;
          nextLinkTitle.href = `project.html?id=${nextId}`;
        }
        if (nextBtnLink) {
          nextBtnLink.href = `project.html?id=${nextId}`;
        }
      }
    } else {
      // Not found
      const mainTitle = document.getElementById('page-main-title');
      if (mainTitle) {
        mainTitle.innerText = "Project Not Found";
      }
    }
  }

"""

# Find the start and end of the modal section
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '// INTERACTIVE PROJECT DETAILS MODAL & TOUCH CAROUSEL SLIDER' in line:
        start_idx = i - 1
    elif '// INTERACTIVE FORMSPREE EMAIL SUBMISSIONS FEEDBACK' in line:
        end_idx = i - 1
        break

if start_idx != -1 and end_idx != -1:
    lines = lines[:start_idx] + [new_content] + lines[end_idx:]
    with open('d:/dev-portfolio/js/main.js', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Successfully updated main.js")
else:
    print("Could not find sections")
