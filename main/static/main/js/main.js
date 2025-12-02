// Smooth & premium UI effects
document.addEventListener('DOMContentLoaded', function () {

    /* -----------------------------
       NAVBAR SCROLL SHADOW & FADE
    ------------------------------ */
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 80) {
            navbar.classList.add('nav-scrolled');
        } else {
            navbar.classList.remove('nav-scrolled');
        }
    });

    const maxTilt = 4; // batas rotasi, biar nggak miring parah
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const percentX = (x / rect.width) - 0.5;  
        const percentY = (y / rect.height) - 0.5;

        const rotateX = percentY * maxTilt;
        const rotateY = percentX * -maxTilt;

        card.style.transform = `
            perspective(900px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            translateY(-3px)
        `;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform =
            "perspective(900px) rotateX(0) rotateY(0) translateY(0)";
    });

    /* -----------------------------
       SECTION FADE-IN ON SCROLL
    ------------------------------ */
    const sections = document.querySelectorAll('section');

    sections.forEach((sec) => {
        sec.classList.add('section-hidden'); 
    });

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('section-visible');
                }
            });
        },
        { threshold: 0.15 }
    );

    sections.forEach((sec) => observer.observe(sec));


    /* -----------------------------
       TYPING EFFECT — Smoother
    ------------------------------ */
    const greeting = document.querySelector('.hero-greeting');
    const text = greeting.textContent.trim();
    greeting.textContent = '';

    let i = 0;
    const type = () => {
        if (i < text.length) {
            greeting.textContent += text[i];
            i++;
            setTimeout(type, 65); // cepat tapi elegan
        }
    };
    setTimeout(type, 800);


    /* -----------------------------
       SKILL TAG MICRO HOVER
    ------------------------------ */
    document.querySelectorAll('.skill-item').forEach((item) => {
        item.addEventListener('mouseenter', () => {
            item.style.transform = 'translateY(-3px)';
            item.style.filter = 'brightness(1.2)';
        });

        item.addEventListener('mouseleave', () => {
            item.style.transform = 'translateY(0)';
            item.style.filter = 'brightness(1)';
        });
    });


    /* -----------------------------
       PROJECT CARD — LIGHT TILT
       (lebih soft dari yang sebelum)
    ------------------------------ */
    document.querySelectorAll('.project-card').forEach((card) => {
        card.addEventListener('mousemove', (e) => {
            const r = card.getBoundingClientRect();
            const x = e.clientX - r.left;
            const y = e.clientY - r.top;

            const moveX = (x - r.width / 2) / 30;
            const moveY = (y - r.height / 2) / 30;

            card.style.transform = `
                perspective(800px) 
                rotateX(${moveY}deg) 
                rotateY(${-moveX}deg)
            `;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(800px) rotateX(0) rotateY(0)';
        });
    });


    /* -----------------------------
       HERO PARALLAX (SUPER SOFT)
    ------------------------------ */
    const hero = document.querySelector('.hero');

    window.addEventListener('scroll', () => {
        if (!hero) return;
        const offset = window.scrollY * -0.15; // lebih soft 
        hero.style.transform = `translateY(${offset}px)`;
    });

});
