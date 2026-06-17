const BUSINESS = {
  name: 'HD הרחקת יונים',
  phoneRawIL: '972528805053',
  phoneDisplay: '052-880-5053',
  whatsappDefaultMessage: 'שלום, אני צריך שירות בהרחקת יונים.'
};

function getWhatsAppDirectUrl(text = BUSINESS.whatsappDefaultMessage) {
  return `https://wa.me/${BUSINESS.phoneRawIL}?text=${encodeURIComponent(text)}`;
}

function buildWhatsAppText(fields) {
  const lines = [BUSINESS.whatsappDefaultMessage];
  if (fields.name) lines.push(`שם: ${fields.name}`);
  if (fields.phone) lines.push(`טלפון: ${fields.phone}`);
  if (fields.city) lines.push(`עיר: ${fields.city}`);
  if (fields.service) lines.push(`שירות: ${fields.service}`);
  if (fields.message) lines.push(`פרטים: ${fields.message}`);
  return encodeURIComponent(lines.join('\n'));
}

function readLeadFields(form) {
  return {
    name: form.querySelector('[name="name"]')?.value?.trim() || '',
    phone: form.querySelector('[name="phone"]')?.value?.trim() || '',
    city: form.querySelector('[name="city"]')?.value?.trim() || '',
    service: form.querySelector('[name="service"]')?.value?.trim() || '',
    message: form.querySelector('[name="message"]')?.value?.trim() || ''
  };
}

function openWhatsAppWith(fields) {
  const url = `https://wa.me/${BUSINESS.phoneRawIL}?text=${buildWhatsAppText(fields)}`;
  window.open(url, '_blank', 'noopener,noreferrer');
}

function closeMobileNav() {
  document.body.classList.remove('nav-open');
  const toggle = document.querySelector('.nav-toggle');
  if (toggle) toggle.setAttribute('aria-expanded', 'false');
}

function initMobileNav() {
  const header = document.querySelector('.site-header');
  if (!header || header.querySelector('.nav-toggle')) return;

  const toggle = document.createElement('button');
  toggle.className = 'nav-toggle';
  toggle.type = 'button';
  toggle.setAttribute('aria-label', 'פתיחת תפריט');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.innerHTML = '<span class="nav-toggle-icon" aria-hidden="true"><span></span><span></span><span></span></span>';

  const overlay = document.createElement('div');
  overlay.className = 'nav-overlay';
  overlay.setAttribute('aria-hidden', 'true');
  document.body.appendChild(overlay);

  const cta = header.querySelector('.header-cta');
  if (cta) {
    header.insertBefore(toggle, cta.nextSibling);
  } else {
    header.appendChild(toggle);
  }

  toggle.addEventListener('click', () => {
    const isOpen = document.body.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.setAttribute('aria-label', isOpen ? 'סגירת תפריט' : 'פתיחת תפריט');
  });

  overlay.addEventListener('click', closeMobileNav);

  header.querySelectorAll('.site-nav a').forEach((link) => {
    link.addEventListener('click', closeMobileNav);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMobileNav();
  });
}

function initScrollHeader() {
  const hero = document.querySelector('.hero');
  if (!hero) return;

  const scrollHeader = document.createElement('div');
  scrollHeader.className = 'scroll-header';
  scrollHeader.innerHTML = `
    <a href="index.html" class="logo">${BUSINESS.name}</a>
    <a href="tel:${BUSINESS.phoneRawIL.replace('972', '0').replace(/^0/, '0')}" class="scroll-header-cta">
      <span aria-hidden="true">📞</span>
      <span>${BUSINESS.phoneDisplay}</span>
    </a>
  `;
  document.body.appendChild(scrollHeader);

  const phoneLink = scrollHeader.querySelector('.scroll-header-cta');
  if (phoneLink) phoneLink.href = 'tel:0528805053';

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const heroBottom = hero.getBoundingClientRect().bottom;
      scrollHeader.classList.toggle('is-visible', heroBottom < 0);
      ticking = false;
    });
  }, { passive: true });
}

function initFaqAccordion() {
  document.querySelectorAll('.faq-item').forEach((item, index) => {
    const dt = item.querySelector('dt');
    const dd = item.querySelector('dd');
    if (!dt || !dd) return;

    if (index === 0) item.classList.add('is-open');

    dt.setAttribute('role', 'button');
    dt.setAttribute('tabindex', '0');
    dt.setAttribute('aria-expanded', index === 0 ? 'true' : 'false');

    const toggle = () => {
      const isOpen = item.classList.toggle('is-open');
      dt.setAttribute('aria-expanded', String(isOpen));
    };

    dt.addEventListener('click', toggle);
    dt.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        toggle();
      }
    });
  });
}

function initScrollReveal() {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;

  const targets = document.querySelectorAll(
    '.section h2, .card, .testimonial, .stats-list li, .why-now-grid li, .region-card, .faq-item'
  );

  targets.forEach((el) => el.classList.add('reveal'));

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  targets.forEach((el) => observer.observe(el));
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.sbtn-wa, .button.wa-direct').forEach((link) => {
    link.href = getWhatsAppDirectUrl();
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
  });

  document.querySelectorAll('.lead-form').forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const fields = readLeadFields(form);
      if (!fields.name) {
        alert('נא למלא שם מלא');
        return;
      }
      if (!fields.phone) {
        alert('נא למלא מספר טלפון');
        return;
      }
      openWhatsAppWith(fields);
    });
  });

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (event) => {
      const id = link.getAttribute('href');
      if (!id || id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      event.preventDefault();
      closeMobileNav();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  initMobileNav();
  initScrollHeader();
  initFaqAccordion();
  initScrollReveal();
});
