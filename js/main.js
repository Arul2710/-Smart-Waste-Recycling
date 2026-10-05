/* ===========================================================
   EcoScrap — shared front-end behaviour
   Vanilla JS only. Every feature degrades gracefully and all
   demo data lives in localStorage / js/data.js.
   =========================================================== */
(function () {
  'use strict';

  var D = window.ECOSCRAP || { categories: [], rates: [], rateCategories: ['All'], locations: [], testimonials: [], posts: [], faq: [], currency: function (n) { return '₹' + n; } };
  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  /* ---------------------------------------------------------
     1. Toast notifications
     --------------------------------------------------------- */
  function toast(message, type, duration) {
    var root = $('#es-toast-root');
    if (!root) {
      root = document.createElement('div');
      root.id = 'es-toast-root';
      document.body.appendChild(root);
    }
    var icons = { success: 'fa-circle-check', error: 'fa-circle-exclamation', info: 'fa-circle-info' };
    var kind = type || 'success';
    var el = document.createElement('div');
    el.className = 'es-toast es-toast--' + kind;
    el.setAttribute('role', 'status');
    el.innerHTML = '<i class="fa-solid ' + (icons[kind] || icons.info) + '"></i><span></span>';
    el.querySelector('span').textContent = message;
    root.appendChild(el);
    window.setTimeout(function () {
      el.classList.add('is-leaving');
      window.setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 300);
    }, duration || 3600);
  }
  window.EcoToast = toast;

  /* ---------------------------------------------------------
     2. localStorage helpers
     --------------------------------------------------------- */
  var Store = {
    get: function (key, fallback) {
      try {
        var raw = localStorage.getItem('ecoscrap-' + key);
        return raw === null ? fallback : JSON.parse(raw);
      } catch (e) { return fallback; }
    },
    set: function (key, value) {
      try { localStorage.setItem('ecoscrap-' + key, JSON.stringify(value)); } catch (e) { /* ignore */ }
    }
  };
  window.EcoStore = Store;

  /* ---------------------------------------------------------
     3. Form validation helpers
     --------------------------------------------------------- */
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var PHONE_RE = /^[0-9+\-\s()]{8,15}$/;

  var Forms = {
    fieldError: function (input, message) {
      var wrap = input.closest('.es-field') || input.parentNode;
      var err = wrap ? wrap.querySelector('.es-error') : null;
      input.setAttribute('aria-invalid', message ? 'true' : 'false');
      if (err) {
        err.textContent = message || '';
        err.classList.toggle('is-visible', !!message);
      }
      return !message;
    },
    validateField: function (input) {
      var value = (input.value || '').trim();
      var label = input.getAttribute('data-label') || 'This field';
      var message = '';

      if (input.hasAttribute('required')) {
        if (input.type === 'checkbox' && !input.checked) message = label + ' is required.';
        else if (input.type !== 'checkbox' && input.type !== 'radio' && !value) message = label + ' is required.';
      }
      if (!message && value) {
        if (input.type === 'email' && !EMAIL_RE.test(value)) message = 'Enter a valid email address.';
        if (input.type === 'tel' && !PHONE_RE.test(value)) message = 'Enter a valid phone number.';
        if (input.dataset.minlen && value.length < Number(input.dataset.minlen)) {
          message = label + ' must be at least ' + input.dataset.minlen + ' characters.';
        }
        if (input.dataset.match) {
          var other = document.getElementById(input.dataset.match);
          if (other && other.value !== value) message = 'Passwords do not match.';
        }
        if (input.type === 'password' && value.length < 6) message = 'Use at least 6 characters.';
      }
      return Forms.fieldError(input, message);
    },
    validate: function (form) {
      var inputs = $$('input, select, textarea', form).filter(function (i) { return i.type !== 'hidden' && !i.disabled; });
      var firstBad = null;
      inputs.forEach(function (input) {
        var ok = Forms.validateField(input);
        if (!ok && !firstBad) firstBad = input;
      });
      if (firstBad) {
        firstBad.focus();
        firstBad.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      return !firstBad;
    },
    alert: function (form, message, type) {
      var box = form.querySelector('[data-form-alert]');
      if (!box) return;
      if (!message) { box.classList.remove('is-visible'); box.innerHTML = ''; return; }
      var icon = type === 'error' ? 'fa-circle-exclamation' : (type === 'info' ? 'fa-circle-info' : 'fa-circle-check');
      box.className = 'es-alert es-alert--' + (type || 'success') + ' is-visible';
      box.innerHTML = '<i class="fa-solid ' + icon + '"></i><span></span>';
      box.querySelector('span').textContent = message;
    }
  };
  window.EcoForms = Forms;

  function wireForms() {
    $$('form[data-validate]').forEach(function (form) {
      form.setAttribute('novalidate', 'novalidate');
      $$('input, select, textarea', form).forEach(function (input) {
        input.addEventListener('blur', function () { Forms.validateField(input); });
        input.addEventListener('input', function () {
          if (input.getAttribute('aria-invalid') === 'true') Forms.validateField(input);
        });
      });
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!Forms.validate(form)) {
          Forms.alert(form, 'Please correct the highlighted fields and try again.', 'error');
          return;
        }
        Forms.alert(form, '');
        if (typeof form._onValid === 'function') form._onValid(new FormData(form));
      });
    });
  }

  /* ---------------------------------------------------------
     4. Navigation: dropdowns, mobile drawer, scroll state
     --------------------------------------------------------- */
  function initDropdowns() {
    var drops = $$('[data-dropdown]');
    drops.forEach(function (drop) {
      var trigger = drop.querySelector('[data-dropdown-trigger]');
      if (!trigger) return;
      var closeTimer;
      function open() {
        window.clearTimeout(closeTimer);
        $$('[data-dropdown]').forEach(function (d) { if (d !== drop) close(d); });
        drop.classList.add('is-open');
        trigger.setAttribute('aria-expanded', 'true');
      }
      function closeNow() {
        drop.classList.remove('is-open');
        trigger.setAttribute('aria-expanded', 'false');
      }
      function close(d) {
        d.classList.remove('is-open');
        var t = d.querySelector('[data-dropdown-trigger]');
        if (t) t.setAttribute('aria-expanded', 'false');
      }
      trigger.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        drop.classList.contains('is-open') ? closeNow() : open();
      });
      trigger.addEventListener('mouseenter', function () { if (window.matchMedia('(min-width: 1280px)').matches) open(); });
      drop.addEventListener('mouseenter', function () { if (window.matchMedia('(min-width: 1280px)').matches) open(); });
      drop.addEventListener('mouseleave', function () {
        if (window.matchMedia('(min-width: 1280px)').matches) {
          closeTimer = window.setTimeout(closeNow, 160);
        }
      });
      trigger.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { closeNow(); trigger.focus(); }
      });
    });
    document.addEventListener('click', function () {
      $$('[data-dropdown]').forEach(function (d) {
        d.classList.remove('is-open');
        var t = d.querySelector('[data-dropdown-trigger]');
        if (t) t.setAttribute('aria-expanded', 'false');
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        $$('[data-dropdown]').forEach(function (d) { d.classList.remove('is-open'); });
        closeMobileMenu();
      }
    });
  }

  function setMenuLock(locked) {
    document.body.style.overflow = locked ? 'hidden' : '';
  }

  function closeMobileMenu() {
    var drawer = $('#es-mobile-nav');
    var burger = $('#es-burger');
    if (!drawer) return;
    drawer.classList.remove('is-open');
    setMenuLock(false);
    // Collapse any open submenus (Dashboard, Home) so reopening starts clean.
    $$('.es-mobile__sub.is-open', drawer).forEach(function (sub) { sub.classList.remove('is-open'); });
    $$('[data-mobile-sub][aria-expanded="true"]', drawer).forEach(function (btn) {
      btn.setAttribute('aria-expanded', 'false');
    });
    if (burger) {
      burger.setAttribute('aria-expanded', 'false');
      var icon = burger.querySelector('i');
      if (icon) { icon.classList.remove('fa-xmark'); icon.classList.add('fa-bars'); }
    }
  }

  function initMobileNav() {
    var burger = $('#es-burger');
    var drawer = $('#es-mobile-nav');
    if (burger && drawer) {
      burger.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var open = drawer.classList.toggle('is-open');
        setMenuLock(open);
        burger.setAttribute('aria-expanded', open ? 'true' : 'false');
        var icon = burger.querySelector('i');
        if (icon) {
          icon.classList.toggle('fa-bars', !open);
          icon.classList.toggle('fa-xmark', open);
        }
      });

      // Close when tapping anywhere outside the open drawer.
      document.addEventListener('click', function (e) {
        if (!drawer.classList.contains('is-open')) return;
        if (drawer.contains(e.target) || burger.contains(e.target)) return;
        closeMobileMenu();
      });

      // Close after following any link inside the drawer.
      $$('a', drawer).forEach(function (a) {
        a.addEventListener('click', function () { window.setTimeout(closeMobileMenu, 120); });
      });
    }
    $$('[data-mobile-sub]').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var target = $('#' + btn.getAttribute('data-mobile-sub'));
        if (!target) return;
        var open = target.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1280) closeMobileMenu();
    });
    window.addEventListener('hashchange', closeMobileMenu);
  }

  function initNavState() {
    var nav = $('.es-nav');
    if (!nav) return;
    var onScroll = function () {
      nav.classList.toggle('is-scrolled', window.scrollY > 8);
      var top = $('#es-top');
      if (top) top.classList.toggle('is-visible', window.scrollY > 420);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    // Mark the active link based on the current file name.
    var file = currentFile();
    $$('.es-nav__link, .es-drop__item, .es-mobile__link').forEach(function (link) {
      var href = (link.getAttribute('href') || '').split('#')[0];
      if (!href) return;
      var target = href.split('/').pop();
      if (target && target === file) {
        link.classList.add('is-active');
        var trigger = link.closest('[data-dropdown]');
        if (trigger) {
          var t = trigger.querySelector('[data-dropdown-trigger]');
          if (t) t.classList.add('is-active');
        }
      }
    });
  }

  /* ---------------------------------------------------------
     4b. Auth-aware navbar
     --------------------------------------------------------- */
  function currentSession() {
    var auth = window.EcoAuth;
    if (auth && typeof auth.session === 'function') {
      try { return auth.session(); } catch (e) { /* fall through */ }
    }
    try {
      return JSON.parse(window.localStorage.getItem('ecoscrap-session') || 'null');
    } catch (e) {
      return null;
    }
  }

  function currentFile() {
    return window.location.pathname.split('/').pop() || 'index.html';
  }

  // Slide the inactivity window forward while the tab is being used.
  function initSessionKeepAlive() {
    var auth = window.EcoAuth;
    if (!auth || typeof auth.touch !== 'function') return;
    var ping = function () { auth.touch(); };
    ['pointerdown', 'keydown'].forEach(function (evt) {
      window.addEventListener(evt, ping, { passive: true });
    });
    document.addEventListener('visibilitychange', function () {
      if (!document.hidden) ping();
    });
  }

  function initAuthState() {
    var guests = $$('[data-auth-guest]');
    var users = $$('[data-auth-user]');
    if (!guests.length && !users.length) return;

    var auth = window.EcoAuth;
    var session = currentSession();
    var isIn = !!session;

    guests.forEach(function (el) { el.hidden = isIn; });
    users.forEach(function (el) { el.hidden = !isIn; });
    if (!isIn) return;

    var name = session.name || (auth && auth.nameFromEmail ? auth.nameFromEmail(session.email) : 'Account');
    var email = session.email || '';
    var initials = auth && auth.initials ? auth.initials(name) : '';
    $$('[data-user-name]').forEach(function (el) { el.textContent = name; });
    $$('[data-user-email]').forEach(function (el) { el.textContent = email; });
    $$('[data-user-initials]').forEach(function (el) { el.textContent = initials; });
    $$('[data-auth-logout]').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        if (auth && auth.logout) {
          auth.logout();
        } else {
          try { window.localStorage.removeItem('ecoscrap-session'); } catch (err) { /* ignore */ }
        }
        toast('You have been logged out.', 'info');
        window.setTimeout(function () { window.location.reload(); }, 500);
      });
    });
  }

  /* ---------------------------------------------------------
     5. Scroll reveal + animated counters
     --------------------------------------------------------- */
  function initReveal() {
    var items = $$('.es-reveal');
    if (!items.length) return;
    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var delay = Number(entry.target.dataset.revealDelay || 0);
          window.setTimeout(function () { entry.target.classList.add('is-visible'); }, delay);
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  function initCounters() {
    var counters = $$('[data-count-to]');
    if (!counters.length) return;
    var run = function (el) {
      var target = Number(el.getAttribute('data-count-to')) || 0;
      var decimals = Number(el.getAttribute('data-count-decimals') || 0);
      var prefix = el.getAttribute('data-count-prefix') || '';
      var suffix = el.getAttribute('data-count-suffix') || '';
      var start = performance.now();
      var dur = 1200;
      function frame(now) {
        var p = Math.min((now - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        var value = target * eased;
        el.textContent = prefix + value.toLocaleString('en-IN', {
          minimumFractionDigits: decimals, maximumFractionDigits: decimals
        }) + suffix;
        if (p < 1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    };
    if (!('IntersectionObserver' in window)) { counters.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { run(entry.target); io.unobserve(entry.target); }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { io.observe(el); });
  }

  /* ---------------------------------------------------------
     6. Category cards (rendered from data.js)
     --------------------------------------------------------- */
  function categoryCard(cat, delay) {
    return '' +
      '<article class="es-card es-card--hover es-reveal" data-reveal-delay="' + (delay || 0) + '">' +
        '<div class="es-card__media">' +
          '<span class="es-card__badge"><i class="fa-solid ' + cat.icon + '"></i> from ' + D.currency(cat.rate) + '/Kg</span>' +
          '<img src="' + cat.img + '" alt="' + cat.alt + '" loading="lazy" decoding="async" width="800" height="500">' +
        '</div>' +
        '<div class="es-card__body">' +
          '<h3 class="es-card__title">' + cat.name + '</h3>' +
          '<p class="es-card__text">' + cat.blurb + '</p>' +
          '<div class="es-card__foot">' +
            '<a href="rate-card.html#' + cat.id + '" class="es-btn es-btn--ghost es-btn--sm es-btn--block">View Rates <i class="fa-solid fa-arrow-right rtl-flip"></i></a>' +
          '</div>' +
        '</div>' +
      '</article>';
  }

  function renderCategories() {
    $$('[data-render="categories"]').forEach(function (host) {
      var limit = Number(host.dataset.limit || 0);
      var list = limit ? D.categories.slice(0, limit) : D.categories;
      host.innerHTML = list.map(function (c, i) { return categoryCard(c, i * 70); }).join('');
    });
  }

  /* ---------------------------------------------------------
     7. Rate card: search, category filter, sort
     --------------------------------------------------------- */
  var rateState = { q: '', cat: 'All', sort: 'category', dir: 1 };

  function rateFiltered() {
    var q = rateState.q.toLowerCase();
    var rows = D.rates.filter(function (r) {
      var okCat = rateState.cat === 'All' || r.category === rateState.cat;
      var okQ = !q || r.material.toLowerCase().indexOf(q) !== -1 || r.category.toLowerCase().indexOf(q) !== -1;
      return okCat && okQ;
    });
    rows.sort(function (a, b) {
      if (rateState.sort === 'price') return (a.price - b.price) * rateState.dir;
      if (rateState.sort === 'material') return a.material.localeCompare(b.material) * rateState.dir;
      return (a.category.localeCompare(b.category) || a.material.localeCompare(b.material));
    });
    return rows;
  }

  function rateRow(r) {
    var badge = { Paper: 'blue', Metal: 'green', Plastic: 'amber', 'E-Waste': 'violet', Appliance: 'slate', Battery: 'red' }[r.category] || 'slate';
    return '<tr>' +
      '<td class="font-medium text-gray-900 dark:text-gray-100">' + r.material + '</td>' +
      '<td><span class="es-badge es-badge--' + badge + '">' + r.category + '</span></td>' +
      '<td class="text-gray-500 dark:text-gray-400">per ' + r.unit + '</td>' +
      '<td class="text-end font-bold text-primary dark:text-primaryLight whitespace-nowrap">' + D.currency(r.price) + '</td>' +
    '</tr>';
  }

  function renderRateTable(targetId) {
    var tbody = document.getElementById(targetId);
    if (!tbody) return;
    var rows = rateFiltered();
    if (!rows.length) {
      tbody.innerHTML = '<tr><td colspan="4"><div class="es-empty"><i class="fa-solid fa-magnifying-glass text-2xl mb-2 block"></i>No materials match your search. Try a different keyword or category.</div></td></tr>';
    } else {
      tbody.innerHTML = rows.map(rateRow).join('');
    }
    var counter = document.querySelector('[data-rate-count]');
    if (counter) counter.textContent = rows.length + ' material' + (rows.length === 1 ? '' : 's') + ' shown';
  }

  function initRateCard() {
    var table = $('#rate-table');
    if (!table) return;
    var tbody = table.querySelector('tbody');

    var chipsHost = $('[data-rate-filters]');
    if (chipsHost) {
      chipsHost.innerHTML = D.rateCategories.map(function (c) {
        return '<button type="button" class="es-chip' + (c === 'All' ? ' is-active' : '') + '" data-rate-cat="' + c + '">' +
          (c === 'All' ? 'All Materials' : c) + '</button>';
      }).join('');
      chipsHost.addEventListener('click', function (e) {
        var btn = e.target.closest('[data-rate-cat]');
        if (!btn) return;
        rateState.cat = btn.getAttribute('data-rate-cat');
        $$('[data-rate-cat]', chipsHost).forEach(function (b) { b.classList.toggle('is-active', b === btn); });
        renderRateTable(tbody.id);
      });
    }

    $$('[data-rate-search]').forEach(function (input) {
      input.addEventListener('input', function () {
        rateState.q = input.value;
        renderRateTable(tbody.id);
      });
    });

    $$('[data-rate-sort]').forEach(function (select) {
      select.addEventListener('change', function () {
        var parts = select.value.split(':');
        rateState.sort = parts[0];
        rateState.dir = parts[1] === 'desc' ? -1 : 1;
        renderRateTable(tbody.id);
      });
    });

    renderRateTable(tbody.id);
  }

  /* ---------------------------------------------------------
     8. Locations: search, filter, selection
     --------------------------------------------------------- */
  function locationCard(loc, delay) {
    var cats = loc.cats.map(function (id) {
      var cat = D.categories.filter(function (c) { return c.id === id; })[0];
      return cat ? cat.name : id;
    });
    var tone = loc.coverage === 'Full Coverage' ? 'green' : (loc.coverage === 'Selected Zones' ? 'blue' : 'amber');
    return '' +
      '<article class="es-card es-card--hover es-reveal" data-location-card data-name="' + loc.name.toLowerCase() + '" data-regions="' + loc.regions.toLowerCase() + '" data-coverage="' + loc.coverage + '" data-reveal-delay="' + (delay || 0) + '">' +
        '<div class="es-card__media es-card__media--wide">' +
          '<span class="es-card__badge es-badge--' + tone + '">' + loc.coverage + '</span>' +
          '<img src="' + loc.img + '" alt="' + loc.alt + '" loading="lazy" decoding="async" width="900" height="506">' +
        '</div>' +
        '<div class="es-card__body">' +
          '<div class="flex items-center gap-3">' +
            '<span class="es-pin"><i class="fa-solid fa-location-dot"></i></span>' +
            '<div><h3 class="es-card__title">' + loc.name + '</h3>' +
            '<p class="text-xs text-gray-500 dark:text-gray-400">' + loc.hours + '</p></div>' +
          '</div>' +
          '<p class="es-card__text">' + loc.regions + '</p>' +
          '<div class="flex flex-wrap gap-1.5">' +
            cats.map(function (c) { return '<span class="es-badge es-badge--slate">' + c + '</span>'; }).join('') +
          '</div>' +
          '<p class="text-xs text-gray-500 dark:text-gray-400"><i class="fa-solid fa-truck-fast me-1.5"></i>' + loc.slots + ' · <i class="fa-solid fa-phone me-1.5"></i>' + loc.phone + '</p>' +
          '<div class="es-card__foot">' +
            '<button type="button" class="es-btn es-btn--primary es-btn--sm es-btn--block" data-select-location="' + loc.name + '">Select This Location</button>' +
          '</div>' +
        '</div>' +
      '</article>';
  }

  function renderLocations() {
    var host = $('[data-render="locations"]');
    if (host) host.innerHTML = D.locations.map(locationCard).join('');

    var search = $('[data-location-search]');
    if (search) {
      search.addEventListener('input', function () {
        filterLocations(search.value, $('[data-location-coverage]') ? $('[data-location-coverage]').value : 'All');
      });
    }
    var coverage = $('[data-location-coverage]');
    if (coverage) {
      coverage.addEventListener('change', function () {
        filterLocations(search ? search.value : '', coverage.value);
      });
    }
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-select-location]');
      if (!btn) return;
      var name = btn.getAttribute('data-select-location');
      Store.set('lastLocation', name);
      toast(name + ' selected. Pickup slot reserved for your next request.', 'success');
      var target = $('[data-location-summary]');
      if (target) {
        target.textContent = 'Selected service area: ' + name;
        target.classList.remove('hidden');
      }
    });
  }

  function filterLocations(query, coverage) {
    var q = (query || '').trim().toLowerCase();
    var shown = 0;
    $$('[data-location-card]').forEach(function (card) {
      var haystack = (card.dataset.name + ' ' + card.dataset.regions).toLowerCase();
      var okQ = !q || haystack.indexOf(q) !== -1;
      var okC = !coverage || coverage === 'All' || card.dataset.coverage === coverage;
      var show = okQ && okC;
      card.style.display = show ? '' : 'none';
      if (show) shown++;
    });
    var empty = $('#locations-empty');
    if (empty) empty.classList.toggle('hidden', shown > 0);
    var count = $('[data-location-count]');
    if (count) count.textContent = shown + ' service area' + (shown === 1 ? '' : 's');
  }

  function initHeroLocationSearch() {
    var form = $('#hero-location-form');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = $('input', form);
      var value = (input.value || '').trim();
      if (value.length < 3) {
        toast('Please enter a valid area, city or PIN code to search.', 'error');
        input.focus();
        return;
      }
      var match = D.locations.filter(function (l) {
        return (l.name + ' ' + l.regions).toLowerCase().indexOf(value.toLowerCase()) !== -1;
      })[0];
      var target = $('#hero-location-result');
      if (match) {
        target.classList.remove('hidden');
        target.innerHTML = '<i class="fa-solid fa-circle-check text-primary"></i> Service available in <strong>' + match.name +
          '</strong> — ' + match.coverage + ', ' + match.slots.toLowerCase() + '.';
        Store.set('lastLocation', match.name);
      } else {
        target.classList.remove('hidden');
        target.innerHTML = '<i class="fa-solid fa-circle-info text-amber-300"></i> We are expanding fast. <strong>' +
          value + '</strong> is not on the live list yet — leave a request and we will notify you.';
      }
      target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
  }

  /* ---------------------------------------------------------
     9. Testimonial slider
     --------------------------------------------------------- */
  function initSlider() {
    $$('[data-slider]').forEach(function (root) {
      var track = $('[data-slider-track]', root);
      var slides = $$('[data-slider-slide]', root);
      var dots = $('[data-slider-dots]', root);
      var index = 0;
      if (!track || !slides.length) return;
      if (dots) {
        dots.innerHTML = slides.map(function (_, i) {
          return '<button type="button" class="es-slider__dot' + (i === 0 ? ' is-active' : '') + '" aria-label="Show testimonial ' + (i + 1) + '"></button>';
        }).join('');
      }
      function go(i) {
        index = (i + slides.length) % slides.length;
        track.style.transform = 'translateX(' + (-100 * index) + '%)';
        if (dots) $$('.es-slider__dot', dots).forEach(function (d, di) { d.classList.toggle('is-active', di === index); });
      }
      var prev = $('[data-slider-prev]', root);
      var next = $('[data-slider-next]', root);
      if (prev) prev.addEventListener('click', function () { go(index - 1); });
      if (next) next.addEventListener('click', function () { go(index + 1); });
      if (dots) dots.addEventListener('click', function (e) {
        var dot = e.target.closest('.es-slider__dot');
        if (dot) go($$('.es-slider__dot', dots).indexOf(dot));
      });
      go(0);
    });
  }

  /* ---------------------------------------------------------
     10. Accordion + tabs
     --------------------------------------------------------- */
  function initAccordions() {
    $$('[data-accordion]').forEach(function (host) {
      host.addEventListener('click', function (e) {
        var btn = e.target.closest('.es-acc__btn');
        if (!btn) return;
        var panel = btn.nextElementSibling;
        var open = panel.classList.contains('is-open');
        $$('.es-acc__panel', host).forEach(function (p) { p.classList.remove('is-open'); });
        $$('.es-acc__btn', host).forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
        if (!open) {
          panel.classList.add('is-open');
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }

  function initTabs() {
    $$('[data-tabs]').forEach(function (host) {
      var btns = $$('[data-tab]', host);
      btns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          var target = btn.getAttribute('data-tab');
          btns.forEach(function (b) {
            b.classList.toggle('is-active', b === btn);
            b.setAttribute('aria-selected', b === btn ? 'true' : 'false');
          });
          $$('[data-tab-panel]', host).forEach(function (p) {
            p.classList.toggle('hidden', p.getAttribute('data-tab-panel') !== target);
          });
        });
      });
    });
  }

  /* ---------------------------------------------------------
     11. Blog listing (optional filter + search)
     --------------------------------------------------------- */
  function postCard(post, delay) {
    var date = new Date(post.date + 'T00:00:00');
    var pretty = date.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
    return '' +
      '<article class="es-card es-card--hover es-reveal" data-post-card data-category="' + post.category.toLowerCase() + '" data-title="' + post.title.toLowerCase() + '" data-reveal-delay="' + (delay || 0) + '">' +
        '<div class="es-card__media es-card__media--wide">' +
          '<span class="es-card__badge">' + post.category + '</span>' +
          '<img src="' + post.img + '" alt="' + post.alt + '" loading="lazy" decoding="async" width="1200" height="675">' +
        '</div>' +
        '<div class="es-card__body">' +
          '<div class="flex items-center gap-3 text-xs text-gray-500 dark:text-gray-400">' +
            '<span><i class="fa-regular fa-calendar me-1.5"></i>' + pretty + '</span>' +
            '<span><i class="fa-regular fa-clock me-1.5"></i>' + post.read + '</span>' +
          '</div>' +
          '<h3 class="es-card__title">' + post.title + '</h3>' +
          '<p class="es-card__text">' + post.excerpt + '</p>' +
          '<div class="es-card__foot flex items-center justify-between gap-3">' +
            '<a href="blog-details.html?post=' + post.slug + '" class="es-btn es-btn--ghost es-btn--sm">Read Article <i class="fa-solid fa-arrow-right rtl-flip"></i></a>' +
          '</div>' +
        '</div>' +
      '</article>';
  }

  function renderPosts() {
    var host = $('[data-render="posts"]');
    if (host) {
      var featured = $('[data-render="featured-post"]');
      var sorted = D.posts.slice().sort(function (a, b) { return a.date < b.date ? 1 : -1; });
      if (featured && sorted.length) {
        var p = sorted[0];
        featured.innerHTML = '' +
          '<a href="blog-details.html?post=' + p.slug + '" class="block group">' +
            '<div class="es-card__media es-card__media--wide rounded-2xl overflow-hidden">' +
              '<span class="es-card__badge">Featured · ' + p.category + '</span>' +
              '<img src="' + p.img + '" alt="' + p.alt + '" loading="lazy" decoding="async" class="w-full h-full object-cover transition duration-700 group-hover:scale-105" width="1200" height="675">' +
            '</div>' +
            '<div class="pt-5">' +
              '<h3 class="text-2xl md:text-3xl font-bold es-title group-hover:text-primary transition">' + p.title + '</h3>' +
              '<p class="es-subtitle mt-3">' + p.excerpt + '</p>' +
              '<span class="inline-flex items-center gap-2 mt-4 text-primary dark:text-primaryLight font-semibold">Read full story <i class="fa-solid fa-arrow-right rtl-flip transition group-hover:translate-x-1"></i></span>' +
            '</div>' +
          '</a>';
        host.innerHTML = sorted.slice(1).map(postCard).join('');
      } else {
        host.innerHTML = sorted.map(postCard).join('');
      }
    }

    // Related posts for blog-details — three recent stories other than the current one.
    var related = $('[data-render="related-posts"]');
    if (related) {
      var currentSlug = (location.search.match(/post=([^&]+)/) || [])[1];
      var pool = D.posts.filter(function (p) { return p.slug !== currentSlug; });
      while (pool.length > 3) { pool.splice(Math.floor(Math.random() * pool.length), 1); }
      related.innerHTML = pool.map(function (p, i) { return postCard(p, i * 70); }).join('');
    }
  }

  function initPostFilter() {
    var host = $('[data-post-filters]');
    if (!host) return;
    var cats = ['All'].concat(D.posts.map(function (p) { return p.category; }).filter(function (v, i, a) { return a.indexOf(v) === i; }));
    host.innerHTML = cats.map(function (c, i) {
      return '<button type="button" class="es-chip' + (i === 0 ? ' is-active' : '') + '" data-post-cat="' + c + '">' +
        (c === 'All' ? 'All Topics' : c) + '</button>';
    }).join('');

    function apply(cat, q) {
      var shown = 0;
      $$('[data-post-card]').forEach(function (card) {
        var okCat = cat === 'All' || card.dataset.category === cat.toLowerCase();
        var okQ = !q || card.dataset.title.indexOf(q) !== -1;
        var show = okCat && okQ;
        card.style.display = show ? '' : 'none';
        if (show) shown++;
      });
      var empty = $('#posts-empty');
      if (empty) empty.classList.toggle('hidden', shown > 0);
    }
    host.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-post-cat]');
      if (!btn) return;
      $$('[data-post-cat]', host).forEach(function (b) { b.classList.toggle('is-active', b === btn); });
      var search = $('[data-post-search]');
      apply(btn.getAttribute('data-post-cat'), search ? search.value.trim().toLowerCase() : '');
    });
    var search = $('[data-post-search]');
    if (search) {
      search.addEventListener('input', function () {
        var active = $('[data-post-cat].is-active', host);
        apply(active ? active.getAttribute('data-post-cat') : 'All', search.value.trim().toLowerCase());
      });
    }
  }

  /* ---------------------------------------------------------
     12. Newsletter
     --------------------------------------------------------- */
  function initNewsletter() {
    var form = $('#newsletter-form');
    if (!form) return;
    form.setAttribute('novalidate', 'novalidate');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = $('input[type="email"]', form);
      var value = (input.value || '').trim();
      if (!EMAIL_RE.test(value)) {
        Forms.fieldError(input, 'Enter a valid email address.');
        input.focus();
        return;
      }
      Forms.fieldError(input, '');
      var list = Store.get('newsletter', []);
      if (list.indexOf(value) === -1) { list.push(value); Store.set('newsletter', list); }
      form.reset();
      toast('Subscribed! Rate updates and recycling tips are on their way to ' + value + '.', 'success');
    });
  }

  /* ---------------------------------------------------------
     13. Back to top
     --------------------------------------------------------- */
  function initBackToTop() {
    if ($('#es-top') || document.body.hasAttribute('data-no-backtop')) return;
    var btn = document.createElement('button');
    btn.id = 'es-top';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Back to top');
    btn.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    document.body.appendChild(btn);
  }

  /* ---------------------------------------------------------
     14. Contact page form
     --------------------------------------------------------- */
  function initContact() {
    var form = $('#contact-form');
    if (!form) return;
    form._onValid = function (data) {
      var messages = Store.get('messages', []);
      messages.unshift({
        name: data.get('name'),
        email: data.get('email'),
        phone: data.get('phone') || '',
        topic: data.get('topic') || 'General',
        message: data.get('message'),
        date: new Date().toISOString().slice(0, 10)
      });
      Store.set('messages', messages.slice(0, 30));
      form.reset();
      Forms.alert(form, 'Thanks ' + (data.get('name') || 'there') + '! Your enquiry has been recorded. Our team responds within one business day.', 'success');
      toast('Message submitted successfully.', 'success');
    };
  }

  /* ---------------------------------------------------------
     14b. Rate estimator (rate-card page)
     --------------------------------------------------------- */
  function initRateCalculator() {
    var form = $('#rate-calculator');
    if (!form) return;
    var materialSel = $('#calc-material', form) || $('[data-calc-material]', form);
    var weightInput = $('#calc-weight', form) || $('[data-calc-weight]', form);
    var result = $('#calc-result');
    function update() {
      if (!materialSel || !weightInput || !result) return;
      var rate = D.rates.filter(function (r) {
        return r.material === materialSel.value;
      })[0];
      var kg = Math.max(Number(weightInput.value) || 0, 0);
      var amount = rate ? kg * rate.price : 0;
      result.classList.toggle('hidden', !rate || kg <= 0);
      if (rate && kg > 0) {
        $('#calc-material-name').textContent = rate.material;
        $('#calc-rate').textContent = D.currency(rate.price) + ' / ' + rate.unit;
        $('#calc-weight-display').textContent = kg + ' ' + rate.unit + '(s)';
        $('#calc-amount').textContent = D.currency(Math.round(amount));
      }
    }
    if (materialSel) {
      materialSel.innerHTML = D.rates.map(function (r) {
        return '<option value="' + r.material + '">' + r.material + ' — ' + D.currency(r.price) + '/' + r.unit + '</option>';
      }).join('');
      materialSel.addEventListener('change', update);
    }
    if (weightInput) weightInput.addEventListener('input', update);
    update();
  }

  /* ---------------------------------------------------------
     15. Boot
     --------------------------------------------------------- */
  function init() {
    if (!$('#es-toast-root')) {
      var r = document.createElement('div');
      r.id = 'es-toast-root';
      document.body.appendChild(r);
    }
    wireForms();
    initDropdowns();
    initMobileNav();
    initNavState();
    initAuthState();
    initSessionKeepAlive();
    renderCategories();
    initRateCard();
    initRateCalculator();
    renderLocations();
    initHeroLocationSearch();
    renderPosts();
    initPostFilter();
    initSlider();
    initAccordions();
    initTabs();
    initNewsletter();
    initContact();
    initBackToTop();
    initReveal();
    initCounters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
