// APP.JS - Project Rendering & Filtering Logic

document.addEventListener('DOMContentLoaded', () => {

  // ==========================================================================
  // DYNAMIC PROJECT RENDERING
  // ==========================================================================
  function renderProjects(filter = 'all') {
    const homeGrid = document.getElementById('projects-grid-container');
    const allGrid = document.getElementById('all-projects-grid');

    if (!homeGrid && !allGrid) return; // Not on a page with projects

    const generateCardHTML = (project, isAllProjectsPage) => {
      let tagsHTML = '';
      if (project.tech && project.tech.length > 0) {
        tagsHTML = `<div class="project-tech-tags">
          ${project.tech.map(t => `<span class="tech-tag ${t.class}">${t.name}</span>`).join('')}
        </div>`;
      }

      let actionsHTML = '';
      if (project.link) {
        actionsHTML = `<div class="project-card-actions">
          <a class="btn-detail-icon" href="${project.link}" aria-label="View Details for ${project.title}">
            View Details
            <span class="icon-circle"><i class="ti ti-arrow-right"></i></span>
          </a>
        </div>`;
      }

      let imageHTML = '';
      if (isAllProjectsPage && project.image) {
        imageHTML = `<div class="project-card-image" style="margin-bottom: 1rem; border-radius: 8px; overflow: hidden; height: 180px; background: #2a2a35;">
          <img src="${project.image}" alt="${project.title} Preview" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8;" />
        </div>`;
      }

      return `
        <div class="project-card glass scroll-fade-card ${project.colorBorder}" data-project="${project.id}">
          ${imageHTML}
          <div class="project-card-header">
            <span class="capstone-badge ${project.categoryClass} monospace">${project.categoryLabel}</span>
            <span class="project-date monospace">${project.date}</span>
          </div>
          <h3 class="project-card-title">
            <span class="dot-indicator ${project.colorDot}"></span>
            ${project.title}
          </h3>
          ${tagsHTML}
          <p class="project-card-desc">${project.description}</p>
          ${actionsHTML}
        </div>
      `;
    };

    if (homeGrid) {
      // Home grid always shows top 5 and ignores filters
      const topProjects = projectsData.slice(0, 5);
      let html = topProjects.map(p => generateCardHTML(p, false)).join('');

      // Add CTA card
      html += `
        <!-- View All Projects CTA -->
        <a href="projects.html" class="project-card glass scroll-fade-card cta-project-card border-purple" aria-label="View All Projects">
          <div class="cta-card-content">
            <i class="ti ti-plus cta-icon"></i>
            <h3 class="cta-title">VIEW ALL PROJECTS</h3>
            <span class="cta-subtitle">See all my work</span>
          </div>
        </a>
      `;
      homeGrid.innerHTML = html;
    }

    if (allGrid) {
      // Apply filter for the full projects page
      let filteredData = projectsData;
      if (filter !== 'all') {
        filteredData = projectsData.filter(p => p.filterCategory === filter);
      }

      let html = filteredData.map(p => generateCardHTML(p, true)).join('');
      allGrid.innerHTML = html;

      // Trigger animations for newly rendered cards
      setTimeout(() => {
        allGrid.querySelectorAll('.scroll-fade-card').forEach((card, index) => {
          card.style.transitionDelay = (index * 50) + 'ms';
          card.classList.add('reveal-active');
        });
        allGrid.querySelectorAll('.tech-tag').forEach((pill, index) => {
          pill.style.transitionDelay = (index * 30) + 'ms';
        });
      }, 50);
    }
  }

  // Render projects initially
  if (typeof projectsData !== 'undefined') {
    renderProjects('all');
  }

  // Filter Buttons Logic (Projects)
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      // Remove active class from all
      filterBtns.forEach(b => b.classList.remove('active'));
      // Add active to clicked
      e.target.classList.add('active');
      // Render
      const filterValue = e.target.getAttribute('data-filter');
      renderProjects(filterValue);
    });
  });

  // Tech Stack View All Logic
  const viewAllTechBtn = document.getElementById('viewAllTechBtn');
  const techGrid = document.getElementById('techGrid');

  if (viewAllTechBtn && techGrid) {
    viewAllTechBtn.addEventListener('click', () => {
      if (techGrid.classList.contains('collapsed')) {
        // Expand
        techGrid.style.maxHeight = techGrid.scrollHeight + 'px';
        techGrid.classList.remove('collapsed');
        viewAllTechBtn.innerText = 'Show Less';
      } else {
        // Collapse
        techGrid.style.maxHeight = '';
        techGrid.classList.add('collapsed');
        viewAllTechBtn.innerText = 'View All Technologies';
      }
    });
  }

  // ==========================================================================
  // PROJECT DATA REPOSITORY (For Modal Manager)
  // ==========================================================================
  const projectData = {
    rfid: {
      title: "RFID Attendance Tracking System (ATS)",
      tags: ["CodeIgniter 4", "PHP", "Tailwind CSS", "DaisyUI", "RFID Hardware"],
      category: "Web & Hardware",
      year: "2025",
      type: "Academic Project",
      duration: "3 Months",
      status: "Completed",
      overview: "A modern, fast, and reliable web-based attendance tracking solution powered by CodeIgniter 4 and RFID technology.",
      challenge: "Manual attendance tracking is prone to errors, time-consuming, and difficult to manage at scale in large educational institutions.",
      approach: "Developed with CodeIgniter 4 and MySQL, the application bridges software databases with physical RFID scanner modules. It features a live tap view for capturing student RFID taps as they enter the room.",
      results: "The system instantly verifies identity status, logs attendance records, and displays real-time activity dashboards. It includes controls for managing students, generating attendance percentages, and exporting dynamic PDF/Excel logs.",
      github: "https://github.com/PinkyBun/RFID-Attendance-Tracking-System-ATS",
      demo: false,
      images: [
        "images/projects/rfid/cover.jpg",
        "images/projects/rfid/screenshot-1.jpg",
        "images/projects/rfid/screenshot-2.jpg",
        "images/projects/rfid/screenshot-3.jpg",
        "images/projects/rfid/screenshot-4.jpg",
        "images/projects/rfid/screenshot-5.jpg",
        "images/projects/rfid/screenshot-6.jpg"
      ]
    },
    ecommerce: {
      title: "E-Commerce Platform (BROWSE AND BUY)",
      tags: ["Laravel 8", "PHP", "MySQL", "Bootstrap 5", "PayPal API"],
      category: "Web Platform",
      year: "2023",
      type: "Academic Project",
      duration: "2 Months",
      status: "Completed",
      overview: "A full-featured, responsive e-commerce web application with a robust admin dashboard.",
      challenge: "Building a secure and scalable e-commerce platform from scratch requires careful handling of user sessions, product inventory, and transactional state.",
      approach: "The platform provides dual user roles, secure authentication, product catalog, and an administrative backend. Includes integration with PayPal for payments and live support through tawk.to and WhatsApp.",
      results: "Customers can browse products, manage shopping carts, apply discount coupons, leave ratings and reviews, and checkout securely. Administrators can manage inventory, coupons, and orders.",
      github: "https://github.com/PinkyBun/E-Commerce-Platform-BROWSE-AND-BUY",
      demo: false,
      images: [
        "images/projects/ecommerce/cover.jpg",
        "images/projects/ecommerce/screenshot-1.png",
        "images/projects/ecommerce/screenshot-2.png",
        "images/projects/ecommerce/screenshot-3.png",
        "images/projects/ecommerce/screenshot-4.png",
        "images/projects/ecommerce/screenshot-5.png",
        "images/projects/ecommerce/screenshot-6.png",
        "images/projects/ecommerce/screenshot-7.png",
        "images/projects/ecommerce/screenshot-8.png",
        "images/projects/ecommerce/screenshot-9.png",
      ]
    },
    inventory: {
      title: "Inventory Management with Billing System",
      tags: ["Laravel 10", "PHP", "MySQL", "Livewire", "Tailwind CSS"],
      category: "Web Application",
      year: "2024",
      type: "Academic Project",
      duration: "2 Months",
      status: "Completed",
      overview: "A robust web application for managing products, point of sales (POS), orders, purchases, and quotations.",
      challenge: "Small businesses often struggle with manual inventory tracking, leading to stockouts or overstock situations due to lack of real-time data.",
      approach: "Built with PHP, Laravel 10, Livewire, and MySQL, the system provides an intuitive POS interface alongside comprehensive tools for managing products, suppliers, customers, and quotations in one centralized platform.",
      results: "Features include interactive dashboard analytics tracking fast-moving items, total sales, and stock levels. It streamlines the tracking of inventory, orders, and sales for small to medium-sized businesses.",
      github: "https://github.com/PinkyBun/Inventory-Management-with-Billing-System",
      demo: false,
      images: [
        "images/projects/inventory/cover.jpg",
        "images/projects/inventory/screenshot-1.png",
        "images/projects/inventory/screenshot-2.png",
        "images/projects/inventory/screenshot-3.png",
        "images/projects/inventory/screenshot-4.png",
        "images/projects/inventory/screenshot-5.png",
        "images/projects/inventory/screenshot-6.png",
        "images/projects/inventory/screenshot-7.png",
      ]
    },
    gym: {
      title: "Gym Attendance Management and Monitoring System",
      tags: ["Laravel 8", "PHP", "MySQL", "DataTables"],
      category: "Web Application",
      year: "2023",
      type: "Academic Project",
      duration: "2 Months",
      status: "Completed",
      overview: "A comprehensive web application designed to streamline member registration, subscription tracking, and attendance monitoring.",
      challenge: "Managing member subscriptions, payments, and facility access manually using spreadsheets leads to inefficiencies and lost revenue.",
      approach: "Built specifically for gym administrators, it provides full CRUD capabilities for managing gym members and automatically categorizes them based on subscription status.",
      results: "Features a modern admin dashboard with interactive DataTables for advanced reporting, attendance logs, and a discount system for eligible members.",
      github: "https://github.com/PinkyBun/Gym-Attendance-Management-and-Monitoring-System",
      demo: false,
      images: [
        "images/projects/gym/cover.jpg",
        "images/projects/gym/screenshot-1.png",
        "images/projects/gym/screenshot-2.png",
        "images/projects/gym/screenshot-3.png",
        "images/projects/gym/screenshot-4.png",
      ]
    },
    datavis: {
      title: "Data Visualization Dashboards",
      tags: ["Power BI", "Excel", "Data Modeling", "ETL Pipelines"],
      category: "Data Analytics",
      year: "2024",
      type: "Data Project",
      duration: "1 Month",
      status: "Completed",
      overview: "A collection of interactive Power BI dashboards built to turn raw, disconnected datasets into clear business intelligence. The collection spans different domains — from biological data exploration to industrial equipment monitoring — showing the ability to adapt one core skill set (data modeling, visualization, and storytelling) across very different types of data and audiences.",
      challenge: "Raw data on its own rarely tells a useful story. Numbers scattered across spreadsheets make it hard to compare categories side by side, track performance over time, or catch warning signs before they become costly problems. Decision-makers need a way to see patterns, rankings, and outliers immediately, without digging through rows of data themselves.",
      approach: "Each dashboard started with understanding what question the data needed to answer, then structuring the data model around that question before any visuals were built. From there, I designed multi-page reports using KPI cards for at - a - glance numbers, ranked bar charts to highlight top and bottom performers, trend and combo charts to show change over time, and interactive filters so users can explore the data on their own terms. A consistent color system and layout were used throughout so every report feels like part of one connected product, not separate one- off charts.",
      results: "The result is a set of dashboards that let users filter, compare, and drill into data in seconds instead of minutes. Patterns that would be invisible in a spreadsheet — like which equipment costs the most to maintain, which assets are nearing critical health, or how categories naturally cluster — become visible at a glance. This turns raw data into a tool decision-makers can actually use day to day, not just a report they read once and set aside.",
      github: false,
      demo: false,
      images: [
        "images/projects/datavis/cover.jpg",
        "images/projects/datavis/screenshot-1.jpg",
        "images/projects/datavis/screenshot-2.jpg"
      ]
    },
    ui: {
      title: "Prototyping & UI/UX Design Projects",
      tags: ["Figma", "Canva", "Wireframing", "Responsive Layouts"],
      category: "Design",
      year: "Ongoing",
      type: "Design Project",
      duration: "Ongoing",
      status: "Active",
      overview: "Information coming soon.",
      challenge: "Information coming soon.",
      approach: "Information coming soon.",
      results: "Information coming soon.",
      github: false,
      demo: false,
      images: [
        "images/projects/ui/cover.jpg",
        "images/projects/ui/screenshot-1.jpg",
        "images/projects/ui/screenshot-2.jpg"
      ]
    }
  };

  // ==========================================================================
  // DYNAMIC PROJECT PAGE POPULATION
  // ==========================================================================
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

      // Icon mapping
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
          githubBtn.style.opacity = '1';
          githubBtn.style.pointerEvents = 'auto';
        } else {
          githubBtn.removeAttribute('href');
          githubBtn.style.opacity = '0.5';
          githubBtn.style.pointerEvents = 'none';
        }
      }

      if (demoBtn) {
        if (data.demo) {
          demoBtn.href = data.demo;
          demoBtn.style.opacity = '1';
          demoBtn.style.pointerEvents = 'auto';
        } else {
          demoBtn.removeAttribute('href');
          demoBtn.style.opacity = '0.5';
          demoBtn.style.pointerEvents = 'none';
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
});
