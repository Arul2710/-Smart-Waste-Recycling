/* ===========================================================
   EcoScrap — admin console behaviour
   Overview analytics, pickup/collector/customer management,
   rate-card editing, weight verification, payouts, blog,
   messages, locations, settings and audit log. Front-end only.
   =========================================================== */
(function () {
  'use strict';

  var D = window.ECOSCRAP || { rates: [], categories: [], locations: [], posts: [], currency: function (n) { return '₹' + n; } };
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var Store = window.EcoStore || {
    get: function (k, f) { try { var r = localStorage.getItem('ecoscrap-' + k); return r === null ? f : JSON.parse(r); } catch (e) { return f; } },
    set: function (k, v) { try { localStorage.setItem('ecoscrap-' + k, JSON.stringify(v)); } catch (e) { /* ignore */ } }
  };
  var toast = window.EcoToast || function () {};
  var Auth = window.EcoAuth || { session: function () { return null; }, logout: function () {}, initials: function () { return 'AD'; } };
  var DD = window.EcoDashData || {};

  var STATUS_CLS = { 'Scheduled': 'blue', 'En Route': 'amber', 'Completed': 'green', 'Cancelled': 'red', 'Paid': 'green', 'Pending': 'amber', 'Published': 'green', 'Draft': 'slate' };

  /* ---------- storage helpers ---------- */
  function pickups() { return DD.seedPickups ? DD.seedPickups() : Store.get('pickups', []); }
  function setPickups(list) { Store.set('pickups', list); }
  function collectors() { return DD.seedCollectors ? DD.seedCollectors() : Store.get('collectors', []); }
  function setCollectors(list) { Store.set('collectors', list); }
  function rates() {
    var list = Store.get('rate-list', null);
    if (!list) { list = D.rates.map(function (r) { return { material: r.material, category: r.category, unit: r.unit, price: r.price }; }); Store.set('rate-list', list); }
    return list;
  }
  function locations() {
    var list = Store.get('loc-list', null);
    if (!list) { list = D.locations.map(function (l) { return { id: l.id, name: l.name, regions: l.regions, coverage: l.coverage, slots: l.slots, phone: l.phone }; }); Store.set('loc-list', list); }
    return list;
  }

  function money(n) { return D.currency(Math.round(Number(n) || 0)); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function badge(status) { return '<span class="es-badge es-badge--' + (STATUS_CLS[status] || 'slate') + '">' + esc(status) + '</span>'; }
  function fmtDate(d) {
    var dt = new Date(d + 'T00:00:00');
    return isNaN(dt) ? d : dt.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
  }
  function isReleased(id) { return Store.get('payout-released', []).indexOf(id) !== -1; }
  function markReleased(id) { var l = Store.get('payout-released', []); if (l.indexOf(id) === -1) { l.push(id); Store.set('payout-released', l); } }
  function payoutStatus(p) { return isReleased(p.id) ? 'Paid' : 'Pending'; }

  /* ---------- search / filter state ---------- */
  var searches = { pickups: '', customers: '', ratecard: '', payouts: '' };
  var pickupFilter = 'All';

  /* ---------- stats ---------- */
  function renderStats() {
    var rows = pickups();
    var active = rows.filter(function (p) { return p.status === 'Scheduled' || p.status === 'En Route'; }).length;
    var emails = {};
    rows.forEach(function (p) { emails[p.email] = 1; });
    var weight = rows.filter(function (p) { return p.status === 'Completed'; }).reduce(function (a, p) { return a + (Number(p.verified) || Number(p.weight) || 0); }, 0);
    var revenue = rows.filter(function (p) { return p.status === 'Completed'; }).reduce(function (a, p) { return a + (Number(p.amount) || 0); }, 0);
    var map = { 'a-requests': String(active), 'a-customers': String(Object.keys(emails).length), 'a-weight': weight.toFixed(0), 'a-revenue': money(revenue) };
    Object.keys(map).forEach(function (k) { $$('[data-stat="' + k + '"]').forEach(function (el) { el.textContent = map[k]; }); });
  }

  /* ---------- charts ---------- */
  function renderCharts() {
    var rows = pickups();
    // weekly bars
    var chart = $('#admin-pickup-chart');
    if (chart) {
      var days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
      var counts = [0, 0, 0, 0, 0, 0, 0];
      rows.forEach(function (p, i) { counts[i % 7] += 1; });
      if (rows.length < 7) counts = [3, 5, 4, 6, 8, 7, 4];
      var max = Math.max.apply(null, counts) || 1;
      chart.innerHTML = days.map(function (d, i) {
        var h = Math.max(6, Math.round((counts[i] / max) * 100));
        return '<div class="es-bar__col" title="' + counts[i] + ' pickups"><div class="es-bar__fill" style="height:' + h + '%"></div><span class="text-xs text-gray-500 dark:text-gray-400">' + d + '</span></div>';
      }).join('');
    }
    // category mix
    var split = $('#admin-category-split');
    if (split) {
      var byCat = {}, total = 0;
      rows.forEach(function (p) {
        var w = Number(p.verified) || Number(p.weight) || 0;
        byCat[p.category] = (byCat[p.category] || 0) + w; total += w;
      });
      if (!total) { byCat = { 'Paper & Cardboard': 220, 'Metal & Aluminum': 140, 'Plastic & Packaging': 90, 'E-Waste': 60, 'Old Appliances': 35, 'Batteries & Recyclables': 20 }; total = 565; }
      split.innerHTML = Object.keys(byCat).sort(function (a, b) { return byCat[b] - byCat[a]; }).map(function (c) {
        var pct = Math.round((byCat[c] / total) * 100);
        return '<div><div class="flex justify-between text-sm mb-1"><span class="text-gray-600 dark:text-gray-300">' + esc(c) + '</span><span class="font-semibold text-gray-900 dark:text-white">' + pct + '%</span></div><div class="es-progress"><span class="es-progress__fill block" style="width:' + pct + '%"></span></div></div>';
      }).join('');
    }
    // revenue chart
    var rev = $('#admin-revenue-chart');
    if (rev) {
      var months = [];
      var base = new Date();
      for (var i = 5; i >= 0; i--) {
        var d = new Date(base.getFullYear(), base.getMonth() - i, 1);
        months.push({ key: d.toISOString().slice(0, 7), label: d.toLocaleDateString('en-IN', { month: 'short' }) });
      }
      var totals = {};
      rows.filter(function (p) { return p.status === 'Completed'; }).forEach(function (p) {
        var k = String(p.date).slice(0, 7);
        totals[k] = (totals[k] || 0) + (Number(p.amount) || 0);
      });
      var rmax = 1;
      months.forEach(function (m) { rmax = Math.max(rmax, totals[m.key] || 0); });
      if (Object.keys(totals).length < 2) { months.forEach(function (m, idx) { totals[m.key] = [18, 26, 21, 34, 30, 43][idx] * 1000; }); rmax = 43000; }
      rev.innerHTML = months.map(function (m) {
        var v = totals[m.key] || 0;
        var h = Math.max(6, Math.round((v / rmax) * 100));
        return '<div class="es-bar__col" title="' + money(v) + '"><div class="es-bar__fill" style="height:' + h + '%"></div><span class="text-xs text-gray-500 dark:text-gray-400">' + m.label + '</span></div>';
      }).join('');
    }
    // ratios
    var ratios = $('#admin-ratios');
    if (ratios) {
      var done = rows.filter(function (p) { return p.status === 'Completed'; }).length;
      var rate = rows.length ? Math.round((done / rows.length) * 100) : 0;
      var metrics = [['Completion rate', rate], ['Payout released', 78], ['Collector utilisation', 64], ['Customer satisfaction', 92]];
      ratios.innerHTML = metrics.map(function (m) {
        return '<div><div class="flex justify-between text-sm mb-1"><span class="text-gray-600 dark:text-gray-300">' + m[0] + '</span><span class="font-semibold text-gray-900 dark:text-white">' + m[1] + '%</span></div><div class="es-progress"><span class="es-progress__fill block" style="width:' + m[1] + '%"></span></div></div>';
      }).join('');
    }
    // city report
    var city = $('#admin-city-report');
    if (city) {
      var byCity = {};
      rows.forEach(function (p) {
        byCity[p.city] = byCity[p.city] || { count: 0, weight: 0, value: 0 };
        byCity[p.city].count++;
        byCity[p.city].weight += Number(p.verified) || Number(p.weight) || 0;
        byCity[p.city].value += Number(p.amount) || 0;
      });
      var maxV = 1;
      Object.keys(byCity).forEach(function (c) { maxV = Math.max(maxV, byCity[c].value); });
      city.innerHTML = Object.keys(byCity).map(function (c) {
        var v = byCity[c];
        var pct = Math.round((v.value / maxV) * 100);
        return '<div class="mb-4 last:mb-0"><div class="flex flex-wrap justify-between gap-2 text-sm mb-1"><span class="font-semibold text-gray-900 dark:text-white">' + esc(c) + '</span><span class="text-gray-500 dark:text-gray-400">' + v.count + ' pickups · ' + v.weight.toFixed(0) + ' kg · ' + money(v.value) + '</span></div><div class="es-progress"><span class="es-progress__fill block" style="width:' + Math.max(4, pct) + '%"></span></div></div>';
      }).join('');
    }
  }

  /* ---------- tables ---------- */
  function renderRecent() {
    var body = $('#admin-recent-body');
    if (!body) return;
    body.innerHTML = pickups().slice(0, 5).map(function (p) {
      return '<tr><td class="font-medium text-gray-900 dark:text-gray-100">' + esc(p.id) + '</td><td>' + esc(p.customer) + '</td><td>' + esc(p.category) + '</td><td>' + badge(p.status) + '</td></tr>';
    }).join('') || '<tr><td colspan="4" class="es-empty">No data.</td></tr>';
  }

  function renderPickups() {
    var body = $('#admin-pickups-body');
    if (!body) return;
    var q = searches.pickups;
    var rows = pickups().filter(function (p) {
      var okF = pickupFilter === 'All' || p.status === pickupFilter;
      var hay = (p.id + ' ' + p.customer + ' ' + p.category + ' ' + p.city).toLowerCase();
      return okF && (!q || hay.indexOf(q) !== -1);
    });
    body.innerHTML = rows.map(function (p) {
      return '<tr><td class="font-medium text-gray-900 dark:text-gray-100">' + esc(p.id) + '</td><td>' + esc(p.customer) + '</td><td>' + esc(p.category) + '</td><td>' + fmtDate(p.date) + ' · ' + esc(p.slot) + '</td><td>' + (p.verified || p.weight) + '</td><td>' + badge(p.status) + '</td><td class="text-end whitespace-nowrap"><button type="button" class="es-btn es-btn--ghost es-btn--sm" data-act="advance" data-id="' + esc(p.id) + '">Advance</button><button type="button" class="es-btn es-btn--ghost es-btn--sm ms-1 text-red-500" data-act="del-pickup" data-id="' + esc(p.id) + '"><i class="fa-solid fa-trash-can"></i></button></td></tr>';
    }).join('') || '<tr><td colspan="7" class="es-empty">No requests match.</td></tr>';
    // filters
    var fhost = $('[data-table-filters="pickups"]');
    if (fhost) {
      var cats = ['All', 'Scheduled', 'En Route', 'Completed', 'Cancelled'];
      fhost.innerHTML = cats.map(function (c) { return '<button type="button" class="es-chip' + (c === pickupFilter ? ' is-active' : '') + '" data-pickup-filter="' + c + '">' + c + '</button>'; }).join('');
    }
  }

  function renderCustomers() {
    var body = $('#admin-customers-body');
    if (!body) return;
    var q = searches.customers;
    var byEmail = {};
    pickups().forEach(function (p) {
      var k = p.email || p.customer;
      if (!byEmail[k]) byEmail[k] = { name: p.customer, email: p.email, city: p.city, count: 0, weight: 0, value: 0 };
      byEmail[k].count++;
      byEmail[k].weight += Number(p.verified) || Number(p.weight) || 0;
      byEmail[k].value += Number(p.amount) || 0;
    });
    var rows = Object.keys(byEmail).map(function (k) { return byEmail[k]; }).filter(function (c) {
      var hay = (c.name + ' ' + c.email + ' ' + c.city).toLowerCase();
      return !q || hay.indexOf(q) !== -1;
    });
    body.innerHTML = rows.map(function (c) {
      var isActive = c.count >= 3;
      var chip = isActive ? '<span class="es-badge es-badge--green">Active</span>' : '<span class="es-badge es-badge--blue">New</span>';
      return '<tr><td><div class="flex items-center gap-3"><span class="w-9 h-9 rounded-full bg-primary/10 text-primary flex items-center justify-center font-semibold">' + esc(Auth.initials(c.name)) + '</span><div><p class="font-medium text-gray-900 dark:text-gray-100">' + esc(c.name) + '</p><p class="text-xs text-gray-400">' + esc(c.email) + '</p></div></div></td><td>' + esc(c.city) + '</td><td>' + c.count + '</td><td>' + c.weight.toFixed(1) + ' kg</td><td class="font-semibold text-primary dark:text-primaryLight">' + money(c.value) + '</td><td>' + chip + '</td></tr>';
    }).join('') || '<tr><td colspan="6" class="es-empty">No customers match.</td></tr>';
  }

  function renderCollectors() {
    var body = $('#admin-collectors-body');
    if (!body) return;
    body.innerHTML = collectors().map(function (c) {
      var cls = c.status === 'Available' ? 'green' : c.status === 'On Route' ? 'amber' : 'slate';
      return '<tr><td class="font-medium text-gray-900 dark:text-gray-100">' + esc(c.name) + '</td><td>' + esc(c.city) + '</td><td>' + esc(c.vehicle) + '</td><td>' + c.assignments + '</td><td><i class="fa-solid fa-star text-amber-400"></i> ' + c.rating.toFixed(1) + '</td><td><span class="es-badge es-badge--' + cls + '">' + esc(c.status) + '</span></td><td class="text-end"><button type="button" class="es-btn es-btn--ghost es-btn--sm text-red-500" data-act="del-collector" data-id="' + esc(c.id) + '"><i class="fa-solid fa-trash-can"></i></button></td></tr>';
    }).join('') || '<tr><td colspan="7" class="es-empty">No collectors.</td></tr>';
  }

  function renderRatecard() {
    var body = $('#admin-ratecard-body');
    if (!body) return;
    var q = searches.ratecard;
    var rows = rates().filter(function (r) { return !q || (r.material + ' ' + r.category).toLowerCase().indexOf(q) !== -1; });
    body.innerHTML = rows.map(function (r, i) {
      return '<tr><td class="font-medium text-gray-900 dark:text-gray-100">' + esc(r.material) + '</td><td>' + esc(r.category) + '</td><td>' + esc(r.unit) + '</td><td class="font-semibold text-primary dark:text-primaryLight">' + money(r.price) + '</td><td class="text-xs text-gray-400">Today</td><td class="text-end whitespace-nowrap"><button type="button" class="es-btn es-btn--ghost es-btn--sm" data-act="edit-rate" data-mat="' + esc(r.material) + '">Edit</button><button type="button" class="es-btn es-btn--ghost es-btn--sm ms-1 text-red-500" data-act="del-rate" data-mat="' + esc(r.material) + '"><i class="fa-solid fa-trash-can"></i></button></td></tr>';
    }).join('') || '<tr><td colspan="6" class="es-empty">No materials match.</td></tr>';
  }

  function renderVerification() {
    var body = $('#admin-verification-body');
    if (!body) return;
    var rows = pickups().filter(function (p) { return p.status === 'En Route' || (p.status === 'Scheduled' && p.verified); });
    if (!rows.length) { body.innerHTML = '<tr><td colspan="7" class="es-empty">Nothing awaiting verification.</td></tr>'; return; }
    body.innerHTML = rows.map(function (p) {
      var claimed = Number(p.weight) || 0;
      var verified = Number(p.verified) || 0;
      var variance = verified ? (((verified - claimed) / claimed) * 100) : 0;
      var result = p.verified ? (Math.abs(variance) <= 5 ? '<span class="es-badge es-badge--green">Matched</span>' : '<span class="es-badge es-badge--amber">Review</span>') : '<span class="es-badge es-badge--slate">Pending</span>';
      return '<tr><td class="font-medium text-gray-900 dark:text-gray-100">' + esc(p.id) + '</td><td>' + esc(p.customer) + '</td><td>' + claimed + ' kg</td><td><input type="number" step="0.1" min="0" value="' + (verified || claimed) + '" class="es-input w-24" data-verify-input="' + esc(p.id) + '"></td><td>' + (verified ? variance.toFixed(1) + '%' : '—') + '</td><td>' + result + '</td><td class="text-end"><button type="button" class="es-btn es-btn--primary es-btn--sm" data-act="verify" data-id="' + esc(p.id) + '">Verify</button></td></tr>';
    }).join('');
  }

  function renderPayments() {
    var body = $('#admin-payments-body');
    if (!body) return;
    var rows = pickups().filter(function (p) { return p.status === 'Completed' && p.amount; });
    body.innerHTML = rows.map(function (p, i) {
      var txn = 'TXN-' + String(90210 + i);
      return '<tr><td class="font-medium text-gray-900 dark:text-gray-100">' + txn + '</td><td>' + esc(p.customer) + '</td><td><span class="es-badge es-badge--slate">' + esc(p.method) + '</span></td><td class="font-semibold text-primary dark:text-primaryLight">' + money(p.amount) + '</td><td class="text-xs text-gray-400">' + fmtDate(p.date) + '</td><td>' + badge(payoutStatus(p)) + '</td></tr>';
    }).join('') || '<tr><td colspan="6" class="es-empty">No payments.</td></tr>';
  }

  function renderLocations() {
    var host = $('#admin-locations-grid');
    if (!host) return;
    host.innerHTML = locations().map(function (l) {
      return '<div class="es-card"><div class="es-card__body"><div class="flex items-start justify-between gap-2"><span class="w-11 h-11 rounded-xl bg-primary/10 text-primary flex items-center justify-center text-lg"><i class="fa-solid fa-map-location-dot"></i></span><button type="button" class="text-gray-400 hover:text-red-500" data-act="del-location" data-id="' + esc(l.id) + '"><i class="fa-solid fa-trash-can"></i></button></div><h3 class="font-semibold text-gray-900 dark:text-white mt-3">' + esc(l.name) + '</h3><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">' + esc(l.regions) + '</p><div class="flex flex-wrap gap-2 mt-3"><span class="es-badge es-badge--green">' + esc(l.coverage) + '</span><span class="es-badge es-badge--slate">' + esc(l.slots) + '</span></div></div></div>';
    }).join('');
  }

  /* ---------- session ---------- */
  function paintUser() {
    var s = Auth.session() || {};
    var name = s.name || 'Admin User';
    var email = s.email || 'admin@ecoscrap.in';
    var initials = Auth.initials(name);
    $$('[data-user-name], [data-user-name-lg]').forEach(function (el) { el.textContent = name; });
    $$('[data-user-email]').forEach(function (el) { el.textContent = email; });
    $$('[data-user-initials], [data-user-initials-lg]').forEach(function (el) { el.textContent = initials; });
  }

  /* ---------- navigation ---------- */
  var VIEW_TITLES = {
    overview: 'Dashboard', pickups: 'Pickup Requests', customers: 'Customers', collectors: 'Collectors',
    ratecard: 'Rate Card', verification: 'Weight Verification', payments: 'Payment History',
    locations: 'Locations', reports: 'Reports & Analytics'
  };
  function navigate(key) {
    var view = $('[data-dash-view="' + key + '"]');
    if (!view) return;
    $$('[data-dash-view]').forEach(function (v) { v.classList.toggle('is-active', v === view); });
    $$('[data-dash-nav]').forEach(function (b) { if (b.tagName !== 'A') b.classList.toggle('is-active', b.getAttribute('data-dash-nav') === key); });
    var title = $('#dash-title'); if (title) title.textContent = VIEW_TITLES[key] || 'Dashboard';
    if (window.location.hash.slice(1) !== key) history.replaceState(null, '', '#' + key);
    closeSidebar();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  function openSidebar() { var s = $('#dash-sidebar'); if (s) s.classList.add('is-open'); var b = $('#dash-backdrop'); if (b) b.classList.add('is-open'); }
  function closeSidebar() { var s = $('#dash-sidebar'); if (s) s.classList.remove('is-open'); var b = $('#dash-backdrop'); if (b) b.classList.remove('is-open'); }
  function initNav() {
    $$('[data-dash-nav]').forEach(function (btn) { btn.addEventListener('click', function () { navigate(btn.getAttribute('data-dash-nav')); }); });
    var burger = $('#dash-burger'); if (burger) burger.addEventListener('click', openSidebar);
    var close = $('#dash-close'); if (close) close.addEventListener('click', closeSidebar);
    var backdrop = $('#dash-backdrop'); if (backdrop) backdrop.addEventListener('click', closeSidebar);
    document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') { closeSidebar(); closeModal(); } });
    window.addEventListener('resize', function () { if (window.innerWidth >= 1024) closeSidebar(); });
    var hash = window.location.hash.slice(1);
    navigate(VIEW_TITLES[hash] ? hash : 'overview');
  }

  /* ---------- modal ---------- */
  var modalEl = null;
  function ensureModal() {
    if (modalEl) return modalEl;
    modalEl = document.createElement('div');
    modalEl.className = 'es-modal';
    modalEl.id = 'admin-modal';
    modalEl.innerHTML = '<div class="es-modal__backdrop" data-modal-close></div><div class="es-modal__panel"><div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white" id="admin-modal-title">Modal</h2><button type="button" class="es-iconbtn" data-modal-close aria-label="Close"><i class="fa-solid fa-xmark"></i></button></div><div class="p-5" id="admin-modal-body"></div></div>';
    document.body.appendChild(modalEl);
    modalEl.addEventListener('click', function (ev) { if (ev.target.closest('[data-modal-close]')) closeModal(); });
    return modalEl;
  }
  function closeModal() { if (modalEl) modalEl.classList.remove('is-open'); }
  function openModal(title, bodyHTML, onSubmit) {
    ensureModal();
    $('#admin-modal-title').textContent = title;
    var body = $('#admin-modal-body');
    body.innerHTML = bodyHTML;
    modalEl.classList.add('is-open');
    var form = $('form', body);
    if (form && onSubmit) {
      form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        var data = {};
        new FormData(form).forEach(function (v, k) { data[k] = typeof v === 'string' ? v.trim() : v; });
        var ok = onSubmit(data);
        if (ok !== false) closeModal();
      });
      setTimeout(function () { var first = $('input,select,textarea', form); if (first) first.focus(); }, 40);
    }
  }
  function fieldHTML(id, label, name, type, value, extra) {
    return '<div class="es-field"><label class="es-label" for="' + id + '">' + label + '</label><input id="' + id + '" name="' + name + '" type="' + type + '" value="' + esc(value == null ? '' : value) + '" class="es-input"' + (extra || '') + '></div>';
  }
  function selectHTML(id, label, name, options, value) {
    return '<div class="es-field"><label class="es-label" for="' + id + '">' + label + '</label><select id="' + id + '" name="' + name + '" class="es-select">' + options.map(function (o) { return '<option' + (o === value ? ' selected' : '') + '>' + esc(o) + '</option>'; }).join('') + '</select></div>';
  }

  function modalPickup() {
    var catOptions = D.categories.map(function (c) { return c.name; });
    openModal('New Pickup Request',
      '<form class="space-y-4">' +
      selectHTML('m-pickup-cat', 'Category', 'category', catOptions, catOptions[0]) +
      '<div class="grid sm:grid-cols-2 gap-4">' + fieldHTML('m-pickup-name', 'Customer name', 'customer', 'text', '', ' required') + fieldHTML('m-pickup-city', 'City', 'city', 'text', (D.locations[0] || {}).name || '', ' required') + '</div>' +
      '<div class="grid sm:grid-cols-3 gap-4">' + fieldHTML('m-pickup-date', 'Date', 'date', 'date', new Date().toISOString().slice(0, 10), ' required') + selectHTML('m-pickup-slot', 'Slot', 'slot', ['Morning', 'Afternoon', 'Evening'], 'Morning') + fieldHTML('m-pickup-weight', 'Weight (kg)', 'weight', 'number', '10', ' min="1" required') + '</div>' +
      fieldHTML('m-pickup-address', 'Pickup address', 'address', 'text', '', ' required') +
      '<div class="flex justify-end gap-2 pt-2"><button type="button" class="es-btn es-btn--ghost" data-modal-close>Cancel</button><button type="submit" class="es-btn es-btn--primary">Create request</button></div></form>',
      function (data) {
        if (!data.customer) { toast('Customer name is required.', 'error'); return false; }
        var list = pickups();
        var id = 'REQ-' + (1051 + list.length);
        var rate = 18;
        list.unshift({ id: id, customer: data.customer, email: data.customer.toLowerCase().replace(/[^a-z0-9]+/g, '.') + '@example.com', category: data.category, material: data.category, date: data.date, slot: data.slot, city: data.city, address: data.address, notes: '', weight: Number(data.weight) || 0, verified: 0, rate: rate, amount: 0, status: 'Scheduled', method: 'UPI' });
        setPickups(list);
        if (DD.logAudit) DD.logAudit('fa-plus', 'Created request ' + id + ' for ' + data.customer);
        toast('Request ' + id + ' created.', 'success');
        refresh();
      });
  }
  function modalCollector() {
    openModal('Add Collector',
      '<form class="space-y-4">' +
      fieldHTML('m-col-name', 'Collector name', 'name', 'text', '', ' required') +
      '<div class="grid sm:grid-cols-2 gap-4">' + fieldHTML('m-col-city', 'City', 'city', 'text', (D.locations[0] || {}).name || '', ' required') + fieldHTML('m-col-vehicle', 'Vehicle no.', 'vehicle', 'text', 'DL-8C-0000', ' required') + '</div>' +
      selectHTML('m-col-status', 'Status', 'status', ['Available', 'On Route', 'Off Duty'], 'Available') +
      '<div class="flex justify-end gap-2 pt-2"><button type="button" class="es-btn es-btn--ghost" data-modal-close>Cancel</button><button type="submit" class="es-btn es-btn--primary">Add collector</button></div></form>',
      function (data) {
        if (!data.name) { toast('Name is required.', 'error'); return false; }
        var list = collectors();
        list.push({ id: 'COL-' + String(list.length + 1).padStart(2, '0'), name: data.name, city: data.city, vehicle: data.vehicle, currentCity: data.city, assignments: 0, rating: 4.6, status: data.status });
        setCollectors(list);
        if (DD.logAudit) DD.logAudit('fa-user-plus', 'Added collector ' + data.name + ' to ' + data.city + ' fleet');
        toast('Collector added.', 'success');
        refresh();
      });
  }
  function modalRate(existing) {
    var catOptions = ['Paper', 'Metal', 'Plastic', 'E-Waste', 'Appliance', 'Battery'];
    openModal(existing ? 'Edit Rate' : 'Add Rate',
      '<form class="space-y-4">' +
      fieldHTML('m-rate-mat', 'Material', 'material', 'text', existing ? existing.material : '', ' required' + (existing ? ' readonly' : '')) +
      '<div class="grid sm:grid-cols-3 gap-4">' + selectHTML('m-rate-cat', 'Category', 'category', catOptions, existing ? existing.category : catOptions[0]) + selectHTML('m-rate-unit', 'Unit', 'unit', ['Kg', 'Piece', 'Each'], existing ? existing.unit : 'Kg') + fieldHTML('m-rate-price', 'Price (₹)', 'price', 'number', existing ? existing.price : '', ' min="0" required') + '</div>' +
      '<div class="flex justify-end gap-2 pt-2"><button type="button" class="es-btn es-btn--ghost" data-modal-close>Cancel</button><button type="submit" class="es-btn es-btn--primary">' + (existing ? 'Save changes' : 'Add rate') + '</button></div></form>',
      function (data) {
        var list = rates();
        if (existing) {
          list.forEach(function (r) { if (r.material === existing.material) { r.category = data.category; r.unit = data.unit; r.price = Number(data.price) || 0; } });
        } else {
          if (list.some(function (r) { return r.material === data.material; })) { toast('That material already exists.', 'error'); return false; }
          list.push({ material: data.material, category: data.category, unit: data.unit, price: Number(data.price) || 0 });
        }
        Store.set('rate-list', list);
        if (DD.logAudit) DD.logAudit('fa-tags', (existing ? 'Updated' : 'Added') + ' rate for ' + data.material + ' at ' + money(data.price));
        toast('Rate saved.', 'success');
        renderRatecard();
      });
  }
  function modalLocation() {
    openModal('Add Location',
      '<form class="space-y-4">' +
      fieldHTML('m-loc-name', 'City name', 'name', 'text', '', ' required') +
      fieldHTML('m-loc-regions', 'Regions covered', 'regions', 'text', '') +
      selectHTML('m-loc-coverage', 'Coverage', 'coverage', ['Full Coverage', 'Selected Zones', 'Partial Coverage'], 'Full Coverage') +
      fieldHTML('m-loc-slots', 'Slots', 'slots', 'text', '4 pickup slots per day') +
      '<div class="flex justify-end gap-2 pt-2"><button type="button" class="es-btn es-btn--ghost" data-modal-close>Cancel</button><button type="submit" class="es-btn es-btn--primary">Add location</button></div></form>',
      function (data) {
        var list = locations();
        list.push({ id: 'loc-' + Date.now(), name: data.name, regions: data.regions, coverage: data.coverage, slots: data.slots, phone: '' });
        Store.set('loc-list', list);
        toast('Location added.', 'success');
        renderLocations();
      });
  }
  /* ---------- actions ---------- */
  function advance(p) {
    var order = ['Scheduled', 'En Route', 'Completed'];
    var idx = order.indexOf(p.status);
    if (idx === -1 || idx === order.length - 1) return;
    p.status = order[idx + 1];
    if (p.status === 'Completed' && !p.amount) { p.verified = p.verified || p.weight; p.amount = Math.round((Number(p.verified) || 0) * p.rate); }
  }
  function initActions() {
    document.addEventListener('click', function (ev) {
      var t = ev.target.closest('[data-act]');
      if (!t) {
        // filters / reset / release-all / open modal / demo handled below
        var fil = ev.target.closest('[data-pickup-filter]');
        if (fil) { pickupFilter = fil.getAttribute('data-pickup-filter'); renderPickups(); return; }
        var open = ev.target.closest('[data-open-modal]');
        if (open) {
          var kind = open.getAttribute('data-open-modal');
          if (kind === 'pickup') modalPickup();
          else if (kind === 'collector') modalCollector();
          else if (kind === 'rate') modalRate(null);
          else if (kind === 'location') modalLocation();
          return;
        }
        if (ev.target.closest('[data-reset-rates]')) {
          Store.set('rate-list', null);
          Store.set('rate-edits', {});
          Store.set('rate-added', []);
          toast('Rates reset to defaults.', 'success');
          renderRatecard();
          return;
        }
        var demo = ev.target.closest('[data-demo-action]');
        if (demo) { toast(demo.getAttribute('data-demo-action') + ' is a demo action.', 'info'); return; }
        if (ev.target.closest('[data-dash-logout]')) {
          Auth.logout();
          toast('Logged out.', 'info');
          window.setTimeout(function () { window.location.href = 'login.html'; }, 600);
        }
        return;
      }
      var act = t.getAttribute('data-act');
      var id = t.getAttribute('data-id');
      var list;
      if (act === 'advance') {
        list = pickups();
        list.forEach(function (p) { if (p.id === id) advance(p); });
        setPickups(list);
        if (DD.logAudit) DD.logAudit('fa-forward', 'Advanced request ' + id);
        toast('Request ' + id + ' updated.', 'success');
        refresh();
      } else if (act === 'del-pickup') {
        setPickups(pickups().filter(function (p) { return p.id !== id; }));
        toast('Request removed.', 'info');
        refresh();
      } else if (act === 'verify') {
        var input = $('[data-verify-input="' + id + '"]');
        var val = input ? Number(input.value) : 0;
        list = pickups();
        list.forEach(function (p) { if (p.id === id) { p.verified = val; p.amount = Math.round(val * p.rate); p.status = 'Completed'; } });
        setPickups(list);
        if (DD.logAudit) DD.logAudit('fa-scale-balanced', 'Verified ' + id + ' at ' + val + ' kg');
        toast('Weight verified for ' + id + '.', 'success');
        refresh();
      } else if (act === 'del-collector') {
        setCollectors(collectors().filter(function (c) { return c.id !== id; }));
        toast('Collector removed.', 'info'); renderCollectors();
      } else if (act === 'edit-rate') {
        var mat = t.getAttribute('data-mat');
        var found = rates().filter(function (r) { return r.material === mat; })[0];
        if (found) modalRate(found);
      } else if (act === 'del-rate') {
        var m = t.getAttribute('data-mat');
        Store.set('rate-list', rates().filter(function (r) { return r.material !== m; }));
        toast('Rate removed.', 'info'); renderRatecard();
      } else if (act === 'del-location') {
        Store.set('loc-list', locations().filter(function (l) { return l.id !== id; }));
        toast('Location removed.', 'info'); renderLocations();
      }
    });
  }

  /* ---------- search wiring ---------- */
  function initSearch() {
    $$('[data-table-search]').forEach(function (input) {
      var key = input.getAttribute('data-table-search');
      input.addEventListener('input', function () {
        searches[key] = input.value.trim().toLowerCase();
        if (key === 'pickups') renderPickups();
        else if (key === 'customers') renderCustomers();
        else if (key === 'ratecard') renderRatecard();
      });
    });
  }

  /* ---------- refresh ---------- */
  function refresh() {
    renderStats(); renderCharts(); renderRecent(); renderPickups(); renderCustomers();
    renderCollectors(); renderRatecard(); renderVerification();
    renderPayments(); renderLocations();
  }

  function init() {
    paintUser(); initNav(); initActions(); initSearch(); refresh();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
