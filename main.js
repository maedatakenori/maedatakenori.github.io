/* TAKENORI MAEDA — main.js */

// Footer year
document.querySelectorAll('#year').forEach(el => {
  el.textContent = new Date().getFullYear();
});

// Lightbox (works page only)
(function () {
  const lightbox = document.getElementById('lightbox');
  if (!lightbox) return;

  const lbImg   = document.getElementById('lightboxImg');
  const lbTitle = document.getElementById('lightboxTitle');
  const lbYear  = document.getElementById('lightboxYear');
  const lbClose = document.getElementById('lightboxClose');
  const lbPrev  = document.getElementById('lightboxPrev');
  const lbNext  = document.getElementById('lightboxNext');

  const items = Array.from(document.querySelectorAll('.work-item'));
  let current = 0;

  function getData(item) {
    const img   = item.querySelector('.work-thumb img');
    const title = item.querySelector('.work-title');
    const year  = item.querySelector('.work-year');
    return {
      src:   img   ? img.src  : '',
      alt:   img   ? img.alt  : '',
      title: title ? title.textContent : '',
      year:  year  ? year.textContent  : '',
    };
  }

  function openAt(index) {
    current = (index + items.length) % items.length;
    const d = getData(items[current]);
    lbImg.src = d.src;
    lbImg.alt = d.alt;
    lbTitle.textContent = d.title;
    lbYear.textContent  = d.year;
    lightbox.classList.add('open');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function close() {
    lightbox.classList.remove('open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  items.forEach((item, i) => {
    item.addEventListener('click', () => openAt(i));
    item.setAttribute('tabindex', '0');
    item.setAttribute('role', 'button');
    item.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') openAt(i);
    });
  });

  lbClose.addEventListener('click', close);
  lbPrev.addEventListener('click',  () => openAt(current - 1));
  lbNext.addEventListener('click',  () => openAt(current + 1));

  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape')     close();
    if (e.key === 'ArrowLeft')  openAt(current - 1);
    if (e.key === 'ArrowRight') openAt(current + 1);
  });

  lightbox.addEventListener('click', e => {
    if (e.target === lightbox) close();
  });

  // Touch swipe
  let tx = 0;
  lightbox.addEventListener('touchstart', e => { tx = e.touches[0].clientX; }, { passive: true });
  lightbox.addEventListener('touchend',   e => {
    const dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 50) openAt(dx < 0 ? current + 1 : current - 1);
  }, { passive: true });
})();
