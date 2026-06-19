// MAIN.JS - Site-Wide Behavior (Nav, Animations, AI Chat)
/**
 * Jasmine A. Nalda - Developer Portfolio Main Interactivity Engine
 * Pure Vanilla JavaScript (No Frameworks)
 */

document.addEventListener("DOMContentLoaded", () => {

  // ==========================================================================
  // PHASE 1: MONOSPACE TERMINAL INTRO SIMULATOR
  // ==========================================================================
  const terminalIntro = document.getElementById('terminal-intro');
  const terminalOutput = document.getElementById('terminal-output');
  const skipIntroBtn = document.getElementById('skip-intro');
  const appContainer = document.getElementById('app-container');

  const introLines = [
    { text: "Initializing portfolio...", prompt: true, delay: 400 },
    { text: "Loading developer profile...", prompt: true, delay: 400 },
    { text: "Hello, World!", prompt: true, delay: 400 },
    { text: "I'm Jasmine A. Nalda", prompt: true, delay: 400 },
    { text: "Full-Stack Developer", prompt: true, delay: 400 }
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
        typingTimeout = setTimeout(typeLine, 50); // typing speed 50ms per character
      } else {
        // Move to the next line after the line's custom delay (400ms pause)
        lineIndex++;
        charIndex = 0;
        typingTimeout = setTimeout(typeLine, lineData.delay);
      }
      
      // Auto scroll terminal output
      terminalOutput.scrollTop = terminalOutput.scrollHeight;
    } else {
      // Intro complete, wait 800ms then transition to main layout
      setTimeout(finishIntro, 800);
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
    sessionStorage.setItem('introPlayed', 'true');
    if (terminalIntro) terminalIntro.classList.add('fade-out');
    if (appContainer) appContainer.classList.remove('app-hidden');
    
    // Tiny delay to allow display reset
    setTimeout(() => {
      if (appContainer) appContainer.classList.add('app-visible');
      // Initialize hero animations and observers once visible
      initHeroTyping();
      initHeroParticles();
      initScrollFadeReveal();
      initTimelineDrawing();
    }, 100);
    
    // Fully remove terminal from DOM after transition finishes
    setTimeout(() => {
      if (terminalIntro) terminalIntro.remove();
    }, 600);
  }

  // Attach intro listeners
  if (skipIntroBtn) {
    skipIntroBtn.addEventListener('click', skipIntro);
  }

  // Check if intro was already played in this session
  if (sessionStorage.getItem('introPlayed') === 'true') {
    isIntroSkipped = true;
    if (terminalIntro) terminalIntro.remove();
    if (appContainer) {
      appContainer.classList.remove('app-hidden');
      setTimeout(() => {
        appContainer.classList.add('app-visible');
        initHeroTyping();
        initHeroParticles();
        initScrollFadeReveal();
        initTimelineDrawing();
      }, 50);
    }
  } else {
    // Page load delay: Entire page fades in, navbar slides down, then terminal starts
    setTimeout(typeLine, 1000);
  }


  // ==========================================================================
  // PHASE 2: HERO CAROUSEL TYPING LOOP
  // ==========================================================================
  const roles = ["Full-Stack Developer", "Mobile App Developer", "Data Visualization", "UI/UX Designer"];
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

    let typingSpeed = isDeleting ? 40 : 60; // 60ms forward typing speed

    if (!isDeleting && roleCharIndex === currentRole.length) {
      // Pause at full word before deleting (1.5s pause)
      typingSpeed = 1500;
      isDeleting = true;
    } else if (isDeleting && roleCharIndex === 0) {
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      typingSpeed = 400; // Pause before typing next word (400ms pause)
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
    // Safety check: do not generate particles if prefers-reduced-motion is active
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return;
    }

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
      const opacity = Math.random() * 0.3 + 0.2; // 0.2 to 0.5 opacity

      particle.style.width = size + 'px';
      particle.style.height = size + 'px';
      particle.style.left = left + '%';
      particle.style.top = top + '%';
      particle.style.opacity = opacity;
      particle.style.animationDuration = duration + 's';
      particle.style.animationDelay = delay + 's';
      particle.style.backgroundColor = 'rgba(167,139,250,0.5)'; // Color spec: rgba(167,139,250,0.5)

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
            <path class="timeline-scroll-draw" fill="none" stroke="rgba(167, 139, 250, 0.6)" stroke-width="2" />
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
      
      // Sync draw path updates smoothly using requestAnimationFrame for scroll events
      let ticking = false;
      const onScroll = () => {
        if (!ticking) {
          window.requestAnimationFrame(() => {
            updatePaths();
            ticking = false;
          });
          ticking = true;
        }
      };
      
      window.addEventListener('scroll', onScroll);
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

    // Stagger tech stack item delay dynamically (60ms per icon inside each category grid)
    document.querySelectorAll('.tech-grid').forEach(grid => {
      const items = grid.querySelectorAll('.tech-item');
      items.forEach((item, index) => {
        item.style.transitionDelay = (index * 60) + 'ms';
      });
    });

    // Stagger certification and project cards dynamically (100ms per card inside grid)
    document.querySelectorAll('.cert-grid, .projects-grid').forEach(grid => {
      const cards = grid.querySelectorAll('.scroll-fade-card');
      cards.forEach((card, index) => {
        card.style.transitionDelay = (index * 100) + 'ms';
      });
    });

    // Stagger contact info items dynamically (100ms per link)
    document.querySelectorAll('.contact-info-panel').forEach(panel => {
      const items = panel.querySelectorAll('.contact-item');
      items.forEach((item, index) => {
        item.classList.add('scroll-fade-card'); // ensure they fade in
        item.style.transitionDelay = (index * 100) + 'ms';
        revealObserver.observe(item); // Fix: Explicitly observe them so they trigger reveal-active!
      });
    });

    // Stagger project tech tag pills dynamically (50ms per pill inside each card)
    document.querySelectorAll('.project-card').forEach(card => {
      const pills = card.querySelectorAll('.tech-tag');
      pills.forEach((pill, index) => {
        pill.style.transitionDelay = (index * 50) + 'ms';
      });
    });

    revealElements.forEach(el => revealObserver.observe(el));
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
