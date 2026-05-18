/**
 * Jasmine A. Nalda - Developer Portfolio Main Interactivity Engine
 * Pure Vanilla JavaScript (No Frameworks)
 */

document.addEventListener('DOMContentLoaded', () => {

  // ==========================================================================
  // PROJECT DATA REPOSITORY (For Modal Manager)
  // ==========================================================================
  const projectData = {
    moneysense: {
      title: "MoneySense Mobile (Capstone)",
      tags: ["Flutter", "Dart", "YOLOv8", "ResNet-18", "ML Kit OCR"],
      description: "MoneySense is a custom accessibility-focused mobile application engineered to assist visually impaired individuals in identifying Philippine banknotes in real time. Built using Flutter and Dart, the core recognition engine integrates a fine-tuned YOLOv8 object detection model for scanning banknote structures and a secondary ResNet-18 classifier for deep verification. The app incorporates Google ML Kit OCR to read textual values on currency notes and translates these inputs into immediate auditory feedback (speech synthesis) for users. Developed as a Capstone Project to promote financial independence for the blind.",
      github: "https://github.com/PinkyBun",
      demo: false,
      images: [
        "images/projects/moneysense/moneysense1.jpg",
        "images/projects/moneysense/moneysense2.jpg",
        "images/projects/moneysense/moneysense3.jpg"
      ]
    },
    rfid: {
      title: "Attendance System with RFID",
      tags: ["Laravel", "PHP", "XAMPP", "RFID Hardware", "SQL"],
      description: "A secure, web-based attendance tracking and monitoring system designed for academic and corporate settings. Developed with Laravel (PHP) and MySQL, the application bridges software databases with physical RFID scanner modules. When a card is tapped, hardware inputs transmit serial data to the Laravel backend endpoint, which instantly verifies identity status, registers timestamps, updates status feeds, and displays real-time activity dashboards. Includes administrative controls for managing rosters, generating attendance percentages, and exporting dynamic PDF/Excel logs.",
      github: "https://github.com/PinkyBun",
      demo: false,
      images: [
        "images/projects/rfid/rfid1.jpg",
        "images/projects/rfid/rfid2.jpg",
        "images/projects/rfid/rfid3.jpg"
      ]
    },
    ecommerce: {
      title: "Full-Stack E-Commerce Website",
      tags: ["Laravel", "PHP", "MySQL", "Bootstrap", "REST API"],
      description: "A comprehensive, production-ready online retail platform designed to deliver smooth user experiences. The backend utilizes Laravel to secure catalog management, inventory levels, cart states, and user sessions. Features an administrative portal where managers can track incoming orders, modify item pricing, and upload product categories. Front-end modules include product search filtering, reviews integration, interactive shopping carts, and a dummy checkout sequence connecting mock credit cards to database transactional records.",
      github: "https://github.com/PinkyBun",
      demo: false,
      images: [
        "images/projects/ecommerce/ecommerce1.jpg",
        "images/projects/ecommerce/ecommerce2.jpg",
        "images/projects/ecommerce/ecommerce3.jpg"
      ]
    },
    inventory: {
      title: "Inventory Management System",
      tags: ["Laravel", "PHP", "SQL", "ChartJS", "XAMPP"],
      description: "A secure database-driven warehouse administration portal designed to track product logistics. Built with PHP, Laravel, and MySQL, the system logs product categories, supplier chains, and dynamic quantities. Incorporates real-time threshold calculations that trigger visual alerts when product quantities fall below minimum levels. Administrative dashboards feature interactive ChartJS graphs tracking weekly transactions, import volumes, and order summaries, helping business owners make quick, informed supply-chain decisions.",
      github: "https://github.com/PinkyBun",
      demo: false,
      images: [
        "images/projects/inventory/inventory1.jpg",
        "images/projects/inventory/inventory2.jpg",
        "images/projects/inventory/inventory3.jpg"
      ]
    },
    gym: {
      title: "Gym Membership Monitoring System",
      tags: ["Laravel", "PHP", "SQL", "XAMPP", "CSS Grid"],
      description: "An administrative web application customized to optimize fitness club operations. The portal allows gym personnel to register members, manage membership package terms, and track payment schedules. The check-in module enables gym visitors to log entry codes, immediately updating active daily rosters on administrative views. The dashboard provides clean summaries of member numbers, subscription expiries, and monthly earnings, replacing manual spreadsheets with a central, automated database.",
      github: "https://github.com/PinkyBun",
      demo: false,
      images: [
        "images/projects/gym/gym1.jpg",
        "images/projects/gym/gym2.jpg",
        "images/projects/gym/gym3.jpg"
      ]
    },
    datavis: {
      title: "Data Visualization Dashboards",
      tags: ["Power BI", "Excel", "Data Modeling", "ETL Pipelines"],
      description: "A collection of interactive analytics dashboards transforming raw transactional spreadsheets into clear, actionable business intelligence models. Processes include extensive ETL data-cleaning routines built in Excel Power Query, removing duplicate entries, normalizing fields, and parsing datasets. Renders critical KPIs, sales progressions, regional markets breakdown, and customer acquisition costs in Power BI, enabling executives to drill down into datasets and make quick, data-driven decisions.",
      github: false,
      demo: false,
      images: [
        "images/projects/datavis/datavis1.jpg",
        "images/projects/datavis/datavis2.jpg",
        "images/projects/datavis/datavis3.jpg"
      ]
    },
    ui: {
      title: "Prototyping & UI/UX Design Projects",
      tags: ["Figma", "Canva", "Wireframing", "Responsive Layouts"],
      description: "A showcase of high-fidelity visual UI layouts, interactive mockups, and mobile prototypes built using Figma and Canva. Focuses on wireframing, creating accessible and logical user flows, and maintaining consistent design languages across screens. Features interactive transitions, custom SVGs, typography guidelines, and responsive layouts designed specifically for diverse mobile and desktop screen sizes, emphasizing strict WCAG color-contrast accessibility compliance.",
      github: false,
      demo: false,
      images: [
        "images/projects/ui/ui1.jpg",
        "images/projects/ui/ui2.jpg",
        "images/projects/ui/ui3.jpg"
      ]
    }
  };

  // ==========================================================================
  // PHASE 1: MONOSPACE TERMINAL INTRO SIMULATOR
  // ==========================================================================
  const terminalIntro = document.getElementById('terminal-intro');
  const terminalOutput = document.getElementById('terminal-output');
  const skipIntroBtn = document.getElementById('skip-intro');
  const appContainer = document.getElementById('app-container');

  const introLines = [
    { text: "Initializing portfolio...", prompt: true, delay: 600 },
    { text: "Loading developer profile...", prompt: true, delay: 600 },
    { text: "Hello, World!", prompt: true, delay: 400 },
    { text: "I'm Jasmine A. Nalda", prompt: true, delay: 400 },
    { text: "Full-Stack Developer", prompt: true, delay: 300 }
  ];

  let lineIndex = 0;
  let charIndex = 0;
  let currentText = "";
  let isIntroSkipped = false;
  let typingTimeout;

  // Render cursor helper
  function appendCursor() {
    const cursor = document.createElement('span');
    cursor.className = 'cursor-blink';
    cursor.id = 'terminal-cursor';
    cursor.innerText = '_';
    terminalOutput.appendChild(cursor);
  }

  function removeCursor() {
    const cursor = document.getElementById('terminal-cursor');
    if (cursor) cursor.remove();
  }

  // Sequentially type out terminal strings char by char
  function typeLine() {
    if (isIntroSkipped) return;

    if (lineIndex < introLines.length) {
      const lineData = introLines[lineIndex];
      
      // Start of a new line
      if (charIndex === 0) {
        removeCursor();
        const lineEl = document.createElement('div');
        lineEl.className = 'terminal-line';
        lineEl.id = `line-${lineIndex}`;
        
        if (lineData.prompt) {
          const promptSpan = document.createElement('span');
          promptSpan.className = 'terminal-prompt';
          promptSpan.innerText = 'root@jn-portfolio:~# ';
          lineEl.appendChild(promptSpan);
        }
        
        const textSpan = document.createElement('span');
        textSpan.id = `text-${lineIndex}`;
        lineEl.appendChild(textSpan);
        terminalOutput.appendChild(lineEl);
        appendCursor();
      }

      const textSpan = document.getElementById(`text-${lineIndex}`);
      if (charIndex < lineData.text.length) {
        textSpan.innerText += lineData.text.charAt(charIndex);
        charIndex++;
        typingTimeout = setTimeout(typeLine, 35); // typing speed
      } else {
        // Move to the next line after the line's custom delay
        lineIndex++;
        charIndex = 0;
        typingTimeout = setTimeout(typeLine, lineData.delay);
      }
      
      // Auto scroll terminal output
      terminalOutput.scrollTop = terminalOutput.scrollHeight;
    } else {
      // Intro complete, transition
      setTimeout(finishIntro, 1200);
    }
  }

  // Instantly skip the terminal and reveal the page
  function skipIntro() {
    isIntroSkipped = true;
    clearTimeout(typingTimeout);
    finishIntro();
  }

  // Smoothly fade out terminal, slide up, and render main website
  function finishIntro() {
    terminalIntro.classList.add('fade-out');
    appContainer.classList.remove('app-hidden');
    
    // Tiny delay to allow display reset
    setTimeout(() => {
      appContainer.classList.add('app-visible');
      // Initialize hero animations and observers once visible
      initHeroTyping();
      initHeroParticles();
      initScrollFadeReveal();
      initTimelineDrawing();
    }, 100);
    
    // Fully remove terminal from DOM after transition finishes
    setTimeout(() => {
      terminalIntro.remove();
    }, 600);
  }

  // Attach intro listeners
  if (skipIntroBtn) {
    skipIntroBtn.addEventListener('click', skipIntro);
  }

  // Start the terminal loop immediately
  typeLine();


  // ==========================================================================
  // PHASE 2: HERO CAROUSEL TYPING LOOP
  // ==========================================================================
  const roles = ["Full-Stack Developer", "Mobile App Developer", "Data Visualization Specialist", "UI/UX Designer"];
  let roleIndex = 0;
  let roleCharIndex = 0;
  let isDeleting = false;
  const typingRoleEl = document.getElementById('typing-role');

  function initHeroTyping() {
    if (!typingRoleEl) return;
    
    const currentRole = roles[roleIndex];
    
    if (isDeleting) {
      typingRoleEl.innerText = currentRole.substring(0, roleCharIndex - 1);
      roleCharIndex--;
    } else {
      typingRoleEl.innerText = currentRole.substring(0, roleCharIndex + 1);
      roleCharIndex++;
    }

    let typingSpeed = isDeleting ? 40 : 80;

    if (!isDeleting && roleCharIndex === currentRole.length) {
      // Pause at full word before deleting
      typingSpeed = 2000;
      isDeleting = true;
    } else if (isDeleting && roleCharIndex === 0) {
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      typingSpeed = 500; // Pause before typing next word
    }

    setTimeout(initHeroTyping, typingSpeed);
  }


  // ==========================================================================
  // MOBILE NAVIGATION HAMBURGER TRIGGERS
  // ==========================================================================
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  function toggleMenu() {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    
    // Toggle aria expanded status
    const isExpanded = hamburger.classList.contains('active');
    hamburger.setAttribute('aria-expanded', isExpanded);
  }

  function closeMenu() {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
  }

  if (hamburger) {
    hamburger.addEventListener('click', toggleMenu);
  }

  navLinks.forEach(link => {
    link.addEventListener('click', closeMenu);
  });


  // ==========================================================================
  // DYNAMIC HEADER SCROLL HOOKS & BACK-TO-TOP TRIGGERS
  // ==========================================================================
  const navbar = document.getElementById('navbar');
  const backToTopBtn = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    // Header sticky transition
    if (navbar) {
      if (scrollY > 20) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }

    // Back to top button visibility
    if (backToTopBtn) {
      if (scrollY > 500) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }
  });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }


  // ==========================================================================
  // LIGHT / DARK MODE DYNAMIC OVERLAYS AND 3D CARD FLIPS
  // ==========================================================================
  const themeToggle = document.getElementById('theme-toggle');
  const themeIconDark = document.getElementById('theme-icon-dark');
  const themeIconLight = document.getElementById('theme-icon-light');
  
  // Set default theme state on initial load
  const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcons(savedTheme);

  function updateThemeIcons(theme) {
    if (theme === 'light') {
      themeIconDark.classList.add('hidden');
      themeIconLight.classList.remove('hidden');
    } else {
      themeIconLight.classList.add('hidden');
      themeIconDark.classList.remove('hidden');
    }
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('portfolio-theme', newTheme);
    updateThemeIcons(newTheme);
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }


  // ==========================================================================
  // ACTIVE NAVIGATION LINK OBSERVER ON SCROLL
  // ==========================================================================
  const sections = document.querySelectorAll('section[id]');
  
  function activeNavHighlight() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120; // offset navbar height
      const sectionId = current.getAttribute('id');
      const activeLink = document.querySelector(`.nav-menu a[href*=${sectionId}]`);

      if (activeLink) {
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          activeLink.classList.add('active');
        } else {
          activeLink.classList.remove('active');
        }
      }
    });
  }

  window.addEventListener('scroll', activeNavHighlight);


  // ==========================================================================
  // FLOATING BACKGROUND PARTICLES (HERO ONLY)
  // ==========================================================================
  function initHeroParticles() {
    const container = document.getElementById('hero-particles');
    if (!container) return;

    // Spawn 18 particles
    const particleCount = 18;
    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement('span');
      particle.className = 'particle';

      const size = Math.random() * 3 + 2; // 2px to 5px
      const left = Math.random() * 100; // 0% to 100%
      const top = Math.random() * 100; // 0% to 100%
      const duration = Math.random() * 4 + 3; // 3s to 7s
      const delay = Math.random() * 5; // 0s to 5s
      const opacity = Math.random() * 0.4 + 0.2; // 0.2 to 0.6

      particle.style.width = size + 'px';
      particle.style.height = size + 'px';
      particle.style.left = left + '%';
      particle.style.top = top + '%';
      particle.style.opacity = opacity;
      particle.style.animationDuration = duration + 's';
      particle.style.animationDelay = delay + 's';

      container.appendChild(particle);
    }
  }

  // ==========================================================================
  // MATHEMATICALLY STRAIGHT SVG SCROLL-DRAWN TIMELINE ENGINE
  // ==========================================================================
  function initTimelineDrawing() {
    const timelines = document.querySelectorAll('.timeline-v2');
    
    timelines.forEach(timeline => {
      // 1. Inject SVG elements if they do not exist
      let svgWrapper = timeline.querySelector('.timeline-svg-wrapper');
      if (!svgWrapper) {
        svgWrapper = document.createElement('div');
        svgWrapper.className = 'timeline-svg-wrapper';
        svgWrapper.innerHTML = `
          <svg class="timeline-svg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1;">
            <path class="timeline-scroll-path" fill="none" stroke="rgba(167, 139, 250, 0.15)" stroke-width="2" />
            <path class="timeline-scroll-draw" fill="none" stroke="var(--accent)" stroke-width="2" />
          </svg>
        `;
        timeline.insertBefore(svgWrapper, timeline.firstChild);
      }

      const bgPath = svgWrapper.querySelector('.timeline-scroll-path');
      const drawPath = svgWrapper.querySelector('.timeline-scroll-draw');
      
      function updatePaths() {
        const dots = timeline.querySelectorAll('.tl-dot');
        if (dots.length < 2) return;
        
        // Hide elements if window matches mobile viewport
        if (window.innerWidth <= 768) {
          svgWrapper.style.display = 'none';
          dots.forEach(dot => dot.classList.add('active'));
          return;
        } else {
          svgWrapper.style.display = 'block';
        }
        
        const timelineRect = timeline.getBoundingClientRect();
        const firstDotRect = dots[0].getBoundingClientRect();
        const lastDotRect = dots[dots.length - 1].getBoundingClientRect();
        
        // Calculate coordinates relative to the timeline parent container
        const x = (firstDotRect.left + firstDotRect.width / 2) - timelineRect.left;
        const startY = (firstDotRect.top + firstDotRect.height / 2) - timelineRect.top;
        const endY = (lastDotRect.top + lastDotRect.height / 2) - timelineRect.top;
        
        // Generate straight SVG path
        const pathData = `M ${x} ${startY} L ${x} ${endY}`;
        bgPath.setAttribute('d', pathData);
        drawPath.setAttribute('d', pathData);
        
        const pathLength = drawPath.getTotalLength();
        drawPath.style.strokeDasharray = pathLength;
        
        // Dynamic scroll drawing height calculations
        const drawHeight = endY - startY;
        const absoluteLineStart = timelineRect.top + startY + window.scrollY;
        
        // Trigger scroll drawing relative to the screen scroll center
        const scrolled = (window.scrollY + window.innerHeight * 0.6) - absoluteLineStart;
        let percent = scrolled / drawHeight;
        percent = Math.max(0, Math.min(1, percent));
        
        drawPath.style.strokeDashoffset = pathLength - (pathLength * percent);
        
        // Dynamically activate pulsing dots as they enter viewport view bounds
        dots.forEach(dot => {
          const dotRect = dot.getBoundingClientRect();
          const dotCenterViewport = dotRect.top + dotRect.height / 2;
          
          if (dotCenterViewport < window.innerHeight * 0.65) {
            dot.classList.add('active');
          } else {
            dot.classList.remove('active');
          }
        });
      }
      
      // Bind scroll and resize listeners for responsiveness
      window.addEventListener('scroll', updatePaths);
      window.addEventListener('resize', updatePaths);
      
      // Trigger paths initially
      setTimeout(updatePaths, 150);
    });
  }

  // ==========================================================================
  // HIGH PERFORMANCE SCROLL-DRIVEN FADE REVEAL ANIMATIONS
  // ==========================================================================
  function initScrollFadeReveal() {
    const revealElements = document.querySelectorAll(
      '.scroll-fade, .scroll-fade-section, .scroll-fade-timeline, .scroll-fade-card'
    );
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal-active');
          observer.unobserve(entry.target); // Trigger only once
        }
      });
    }, {
      threshold: 0.1, // Trigger when 10% is visible
      rootMargin: "0px 0px -40px 0px"
    });

    // Stagger tech stack item delay dynamically (50ms per item inside each category grid)
    document.querySelectorAll('.tech-grid').forEach(grid => {
      const items = grid.querySelectorAll('.tech-item');
      items.forEach((item, index) => {
        item.style.transitionDelay = (index * 50) + 'ms';
      });
    });

    revealElements.forEach(el => revealObserver.observe(el));
  }


  // ==========================================================================
  // INTERACTIVE PROJECT DETAILS MODAL & TOUCH CAROUSEL SLIDER
  // ==========================================================================
  const modal = document.getElementById('project-modal');
  const modalClose = document.getElementById('modal-close');
  const slidesWrapper = document.getElementById('modal-slides-wrapper');
  const prevBtn = document.getElementById('slider-prev');
  const nextBtn = document.getElementById('slider-next');
  const dotsContainer = document.getElementById('slider-indicators');
  
  const mTitle = document.getElementById('modal-project-title');
  const mTags = document.getElementById('modal-tech-tags');
  const mDesc = document.getElementById('modal-project-description');
  const mBtnGithub = document.getElementById('modal-btn-github');
  const mBtnDemo = document.getElementById('modal-btn-demo');

  let currentSlideIndex = 0;
  let totalSlidesCount = 0;
  let touchStartX = 0;
  let touchEndX = 0;

  // Bind project cards
  window.openProjectModal = function(projectId) {
    const data = projectData[projectId];
    if (!data) return;

    // Reset carousel indexes
    currentSlideIndex = 0;
    totalSlidesCount = data.images.length;

    // Load Text Content
    mTitle.innerText = data.title;
    mDesc.innerText = data.description;

    // Load Tech Tags
    mTags.innerHTML = '';
    data.tags.forEach(tag => {
      const tagSpan = document.createElement('span');
      tagSpan.className = 'tech-tag';
      tagSpan.innerText = tag;
      mTags.appendChild(tagSpan);
    });

    // Configure External CTA Buttons
    if (data.github) {
      mBtnGithub.href = data.github;
      mBtnGithub.classList.remove('disabled');
      mBtnGithub.style.display = 'inline-flex';
    } else {
      mBtnGithub.classList.add('disabled');
      mBtnGithub.style.display = 'none';
    }

    if (data.demo) {
      mBtnDemo.href = data.demo;
      mBtnDemo.classList.remove('disabled');
      mBtnDemo.style.display = 'inline-flex';
    } else {
      mBtnDemo.classList.add('disabled');
      mBtnDemo.style.display = 'none';
    }

    // Load Carousel Images
    slidesWrapper.innerHTML = '';
    data.images.forEach(imgSrc => {
      const img = document.createElement('img');
      img.src = imgSrc;
      img.alt = `${data.title} Interface View`;
      img.className = 'slide-img';
      
      // Fallback in case actual generated files fail, render CSS styled error panel
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

    // Generate Indicator Dots
    dotsContainer.innerHTML = '';
    for (let i = 0; i < totalSlidesCount; i++) {
      const dot = document.createElement('div');
      dot.className = `dot ${i === 0 ? 'active' : ''}`;
      dot.addEventListener('click', () => navigateToSlide(i));
      dotsContainer.appendChild(dot);
    }

    // Show modal with accessibility attribute changes
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden'; // Stop background scroll
    modal.focus();

    // Render original positions
    updateSliderPosition();
  };

  function closeModal() {
    modal.classList.add('hidden');
    document.body.style.overflow = ''; // Resume normal scrolling
  }

  // Slider navigation logic
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
    
    // Highlight indicator dots
    const dots = dotsContainer.querySelectorAll('.dot');
    dots.forEach((dot, idx) => {
      if (idx === currentSlideIndex) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  // Slider Click Hooks
  if (prevBtn) prevBtn.addEventListener('click', () => navigateToSlide(currentSlideIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => navigateToSlide(currentSlideIndex + 1));

  // Modal Close Bindings
  if (modalClose) modalClose.addEventListener('click', closeModal);
  
  // Close when clicking outside of modal card
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  // Keyboard accessibility closing and navigation
  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('hidden')) {
      if (e.key === 'Escape') {
        closeModal();
      } else if (e.key === 'ArrowRight') {
        navigateToSlide(currentSlideIndex + 1);
      } else if (e.key === 'ArrowLeft') {
        navigateToSlide(currentSlideIndex - 1);
      }
    }
  });

  // Swipe support on Mobile Slider
  slidesWrapper.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  slidesWrapper.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipeGesture();
  }, { passive: true });

  function handleSwipeGesture() {
    const swipeThreshold = 50;
    if (touchStartX - touchEndX > swipeThreshold) {
      // Swiped Left -> Next
      navigateToSlide(currentSlideIndex + 1);
    } else if (touchEndX - touchStartX > swipeThreshold) {
      // Swiped Right -> Prev
      navigateToSlide(currentSlideIndex - 1);
    }
  }


  // ==========================================================================
  // INTERACTIVE FORMSPREE EMAIL SUBMISSIONS FEEDBACK
  // ==========================================================================
  const contactForm = document.getElementById('contact-form');
  const formSubmitBtn = document.getElementById('form-submit');
  const formSuccessAlert = document.getElementById('form-success');
  const formErrorAlert = document.getElementById('form-error');

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      // Reset feedback indicators
      formSuccessAlert.classList.add('hidden');
      formErrorAlert.classList.add('hidden');
      
      // Update submitting button state
      const originalBtnText = formSubmitBtn.innerHTML;
      formSubmitBtn.disabled = true;
      formSubmitBtn.innerHTML = 'Sending...';

      const formData = new FormData(contactForm);
      const endpoint = contactForm.getAttribute('action');

      // Prevent submit if placeholder Form ID is not replaced
      if (endpoint.includes('YOUR_FORM_ID')) {
        setTimeout(() => {
          formSubmitBtn.disabled = false;
          formSubmitBtn.innerHTML = originalBtnText;
          formErrorAlert.innerHTML = '<span class="alert-icon">✗</span> Formspree is in demo mode! Replace "YOUR_FORM_ID" in index.html to deploy live submissions.';
          formErrorAlert.classList.remove('hidden');
        }, 800);
        return;
      }

      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          body: formData,
          headers: {
            'Accept': 'application/json'
          }
        });

        if (response.ok) {
          formSuccessAlert.classList.remove('hidden');
          contactForm.reset();
        } else {
          formErrorAlert.classList.remove('hidden');
        }
      } catch (error) {
        formErrorAlert.classList.remove('hidden');
      } finally {
        formSubmitBtn.disabled = false;
        formSubmitBtn.innerHTML = originalBtnText;
      }
    });
  }

});
