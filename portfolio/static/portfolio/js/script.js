/* ═══════════════════════════════════════════════════════
   PORTFOLIO — Main JavaScript
   Features: Particles, Typing, Scroll, Theme, Projects
   ═══════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

    // ═══════ LOADING SCREEN ═══════
    window.addEventListener('load', () => {
        setTimeout(() => {
            document.getElementById('loading').classList.add('hide');
        }, 1200);
    });

    // ═══════ DARK / LIGHT THEME TOGGLE ═══════
    const themeToggle = document.getElementById('theme-toggle');
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    themeToggle.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        updateThemeIcon(next);
    });

    function updateThemeIcon(theme) {
        const icon = themeToggle.querySelector('i');
        icon.className = theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
    }

    // ═══════ SCROLL PROGRESS BAR ═══════
    window.addEventListener('scroll', () => {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = (scrollTop / scrollHeight) * 100;
        document.getElementById('scrollIndicator').style.width = progress + '%';
    });

    // ═══════ NAVBAR — Scroll shadow + active link ═══════
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section, .hero');

    window.addEventListener('scroll', () => {
        // Shadow on scroll
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Active nav link
        let current = '';
        sections.forEach(section => {
            const top = section.offsetTop - 100;
            if (window.scrollY >= top) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('data-section') === current) {
                link.classList.add('active');
            }
        });
    });

    // ═══════ MOBILE NAV HAMBURGER ═══════
    const hamburger = document.getElementById('nav-hamburger');
    const navLinksContainer = document.getElementById('nav-links');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinksContainer.classList.toggle('open');
    });

    // Close mobile nav on link click
    navLinksContainer.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinksContainer.classList.remove('open');
        });
    });

    // ═══════ TYPING ANIMATION ═══════
    const typingEl = document.getElementById('typing-text');
    const roles = [
        'Full Stack Developer',
        'AI Enthusiast',
        'Cyber Security Geek',
        'Python Developer',
        'Django Expert',
        'Open Source Contributor'
    ];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 80;

    function type() {
        const currentRole = roles[roleIndex];

        if (isDeleting) {
            typingEl.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 40;
        } else {
            typingEl.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 80;
        }

        if (!isDeleting && charIndex === currentRole.length) {
            isDeleting = true;
            typingSpeed = 1800; // Pause at end
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typingSpeed = 400; // Pause before next word
        }

        setTimeout(type, typingSpeed);
    }

    type();

    // ═══════ SCROLL REVEAL ANIMATION ═══════
    const revealElements = document.querySelectorAll('.glass-card, .section-header, .project-card, .timeline-node, .stat-item, .contact-card, .contact-form, .resume-section, .hero-code-block');

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    revealElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = `opacity 0.6s ease ${index * 0.05}s, transform 0.6s ease ${index * 0.05}s`;
        revealObserver.observe(el);
    });

    // ═══════ STATS COUNTER ANIMATION ═══════
    const statNumbers = document.querySelectorAll('.stat-number');
    let statsCounted = false;

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !statsCounted) {
                statsCounted = true;
                statNumbers.forEach(stat => {
                    const target = parseInt(stat.getAttribute('data-count'));
                    let current = 0;
                    const increment = target / 40;
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            current = target;
                            clearInterval(timer);
                        }
                        stat.textContent = Math.floor(current);
                    }, 40);
                });
            }
        });
    }, { threshold: 0.3 });

    const statsSection = document.querySelector('.about-stats');
    if (statsSection) statsObserver.observe(statsSection);

    // ═══════ SKILL PROGRESS BARS ═══════
    const progressBars = document.querySelectorAll('.progress-fill');

    const progressObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const width = entry.target.getAttribute('data-width');
                entry.target.style.width = width + '%';
                progressObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    progressBars.forEach(bar => progressObserver.observe(bar));

    // ═══════ FETCH PROJECTS FROM API ═══════
    fetch('/api/projects/')
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById('projects-container');
            container.innerHTML = '';

            if (data.length === 0) {
                container.innerHTML = '<p style="color: var(--text-muted); text-align: center;">No projects found.</p>';
                return;
            }

            data.forEach((proj, index) => {
                const card = document.createElement('div');
                card.className = 'project-card';
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                card.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;

                const tags = proj.tech_stack
                    ? proj.tech_stack.split(',').map(t => `<span class="project-tag">${t.trim()}</span>`).join('')
                    : '';

                card.innerHTML = `
                    <div class="project-card-header">
                        <div class="project-card-icon"><i class="fa-solid fa-folder-open"></i></div>
                        ${proj.github_link ? `<a href="${proj.github_link}" target="_blank" class="project-card-link" title="View on GitHub"><i class="fa-brands fa-github"></i></a>` : ''}
                    </div>
                    <h3>${proj.title}</h3>
                    <p>${proj.description}</p>
                    <div class="project-tags">${tags}</div>
                `;

                container.appendChild(card);

                // Trigger animation
                requestAnimationFrame(() => {
                    requestAnimationFrame(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    });
                });
            });
        })
        .catch(err => {
            console.error('Error fetching projects:', err);
            document.getElementById('projects-container').innerHTML =
                '<p style="color: var(--text-muted); text-align: center;">Failed to load projects. Please try refreshing.</p>';
        });

    // ═══════ CONTACT FORM ═══════
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = document.getElementById('contact-submit-btn');
            const status = document.getElementById('form-status');

            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';
            btn.disabled = true;

            const payload = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value,
            };

            fetch('/api/contact/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload),
            })
            .then(res => res.json())
            .then(data => {
                status.textContent = data.message;
                status.style.color = data.status === 'success' ? '#10b981' : '#ef4444';
                if (data.status === 'success') contactForm.reset();
                btn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Send Message';
                btn.disabled = false;
            })
            .catch(err => {
                status.textContent = 'An error occurred. Please try again.';
                status.style.color = '#ef4444';
                btn.innerHTML = '<i class="fa-solid fa-paper-plane"></i> Send Message';
                btn.disabled = false;
            });
        });
    }

    // ═══════ SMOOTH SCROLL FOR ANCHOR LINKS ═══════
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ═══════ PARTICLES BACKGROUND ═══════
    const canvas = document.getElementById('particles-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let particles = [];
        let mouseX = 0;
        let mouseY = 0;

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }

        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        class Particle {
            constructor() {
                this.reset();
            }

            reset() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2 + 0.5;
                this.speedX = (Math.random() - 0.5) * 0.5;
                this.speedY = (Math.random() - 0.5) * 0.5;
                this.opacity = Math.random() * 0.4 + 0.1;
            }

            update() {
                this.x += this.speedX;
                this.y += this.speedY;

                if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
                if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(99, 102, 241, ${this.opacity})`;
                ctx.fill();
            }
        }

        // Create particles
        const particleCount = Math.min(60, Math.floor((canvas.width * canvas.height) / 15000));
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }

        function connectParticles() {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < 150) {
                        const opacity = (1 - dist / 150) * 0.12;
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(99, 102, 241, ${opacity})`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            connectParticles();
            requestAnimationFrame(animate);
        }

        animate();
    }
});
