/* ===========================================================
   EcoScrap — customer dashboard behaviour
   Renders demo bookings/payouts from localStorage, handles the
   schedule form, sidebar navigation, filters and profile forms.
   =========================================================== */
(function () {
  'use strict';

  var D = window.ECOSCRAP || { categories: [], rates: [], locations: [], currency: function (n) { return '₹' + n; } };
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var Store = window.EcoStore || {
    get: function (k, f) { try { var r = localStorage.getItem('ecoscrap-' + k); return r === null ? f : JSON.parse(r); } catch (e) { return f; } },
    set: function (k, v) { try { localStorage.setItem('ecoscrap-' + k, JSON.stringify(v)); } catch (e) { /* ignore */ } }
  };
  var toast = window.EcoToast || function () {};
  var Auth = window.EcoAuth || { nameFromEmail: function () { return 'Green Guest'; }, initials: function () { return 'GG'; }, session: function () { return null; }, logout: function () {} };

  var STATUS_META = {
    'Scheduled': { cls: 'blue', icon: 'fa-calendar-check', step: 1 },
    'En Route': { cls: 'amber', icon: 'fa-truck-fast', step: 3 },
    'Completed': { cls: 'green', icon: 'fa-circle-check', step: 5 },
    'Cancelled': { cls: 'red', icon: 'fa-circle-xmark', step: 0 }
  };
  var STATUSES = ['Scheduled', 'En Route', 'Completed', 'Cancelled'];

  function todayISO() { return new Date().toISOString().slice(0, 10); }
  function monthKey(d) { return String(d).slice(0, 7); }

  /* ---------- seeding ---------- */
  function seedPickups() {
    if (window.EcoDashData) return window.EcoDashData.seedPickups();
    var existing = Store.get('pickups', null);
    if (existing && existing.length) return existing;
    Store.set('pickups', []);
    return [];
  }

  function myEmail() { return (getProfile().email || (Auth.session() || {}).email || 'demo@ecoscrap.in').toLowerCase(); }
  function myRows() { return seedPickups().filter(function (p) { return String(p.email || '').toLowerCase() === myEmail(); }); }

  function getProfile() {
    var s = Auth.session() || {};
    var stored = Store.get('profile', null);
    if (stored) return stored;
    var profile = {
      name: s.name || 'Green User',
      email: s.email || 'demo@ecoscrap.in',
      phone: '+91 98100 11223',
      city: 'Delhi NCR'
    };
    Store.set('profile', profile);
    return profile;
  }

  function seedAddresses() {
    var a = Store.get('addresses', null);
    if (a && a.length) return a;
    a = [
      { id: 'ad-1', label: 'Home', city: 'Delhi NCR', address: 'B-42, Green Apartments, Okhla, New Delhi 110020', primary: true },
      { id: 'ad-2', label: 'Office', city: 'Delhi NCR', address: '3rd Floor, Tech Park, Nehru Place, New Delhi 110019', primary: false }
    ];
    Store.set('addresses', a);
    return a;
  }

  function seedNotifs() {
    var n = Store.get('notifs', null);
    if (n && n.length) return n;
    n = [
      { id: 'n1', icon: 'fa-truck-fast', title: 'Collector dispatched for REQ-1042', time: '12 minutes ago', read: false },
      { id: 'n2', icon: 'fa-money-bill-wave', title: 'Payout of ₹325 credited to your UPI', time: 'Yesterday', read: false },
      { id: 'n3', icon: 'fa-tags', title: 'Copper rates rose 4% today', time: '2 days ago', read: false },
      { id: 'n4', icon: 'fa-circle-check', title: 'Pickup REQ-1039 verified at 11.6 kg', time: '4 days ago', read: true }
    ];
    Store.set('notifs', n);
    return n;
  }

  /* ---------- helpers ---------- */
  function money(n) { return D.currency(Math.round(Number(n) || 0)); }
  function statusBadge(status) {
    var m = STATUS_META[status] || STATUS_META['Scheduled'];
    return '<span class="es-badge es-badge--' + m.cls + '"><i class="fa-solid ' + m.icon + '"></i> ' + status + '</span>';
  }
  function formatDate(d) {
    var dt = new Date(d + 'T00:00:00');
    if (isNaN(dt)) return d;
    return dt.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
  }

  /* ---------- session / user ---------- */
  function paintUser() {
    var s = Auth.session() || {};
    var p = getProfile();
    var name = p.name || s.name || 'Green User';
    var email = p.email || s.email || 'demo@ecoscrap.in';
    var initials = Auth.initials(name);
    $$('[data-user-name]').forEach(function (e) { e.textContent = name; });
    $$('[data-user-email]').forEach(function (e) { e.textContent = email; });
    $$('[data-user-initials], [data-user-initials-lg]').forEach(function (e) { e.textContent = initials; });
  }

  /* ---------- stats ---------- */
  function renderStats() {
    var pickups = myRows();
    var active = pickups.filter(function (p) { return p.status !== 'Cancelled'; });
    var weight = active.reduce(function (a, p) { return a + (Number(p.verified) || Number(p.weight) || 0); }, 0);
    var earnings = active.reduce(function (a, p) { return a + (Number(p.amount) || 0); }, 0);
    var co2 = weight * 1.4;
    var map = {
      pickups: String(active.length),
      weight: weight.toFixed(1),
      earnings: money(earnings),
      co2: co2.toFixed(1)
    };
    Object.keys(map).forEach(function (k) {
      $$('[data-stat="' + k + '"]').forEach(function (e) { e.textContent = map[k]; });
    });
  }

  /* ---------- tables ---------- */
  function renderRecent() {
    var body = $('#cust-recent-body');
    if (!body) return;
    var rows = myRows().slice(0, 5);
    body.innerHTML = rows.map(function (p) {
      return '<tr>' +
        '<td class="font-medium text-gray-900 dark:text-gray-100">' + p.id + '</td>' +
        '<td>' + p.material + '</td>' +
        '<td>' + (p.verified || p.weight) + ' kg</td>' +
        '<td class="font-semibold text-primary dark:text-primaryLight">' + (p.amount ? money(p.amount) : '—') + '</td>' +
        '<td>' + statusBadge(p.status) + '</td>' +
        '</tr>';
    }).join('') || '<tr><td colspan="5" class="es-empty">No pickups yet.</td></tr>';
  }

  var reqFilter = 'All';
  function renderRequestFilters() {
    var host = $('#cust-req-filters');
    if (!host) return;
    var cats = ['All'].concat(STATUSES);
    host.innerHTML = cats.map(function (c) {
      return '<button type="button" class="es-chip' + (c === reqFilter ? ' is-active' : '') + '" data-req-filter="' + c + '">' + (c === 'All' ? 'All' : c) + '</button>';
    }).join('');
    host.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-req-filter]');
      if (!btn) return;
      reqFilter = btn.getAttribute('data-req-filter');
      $$('[data-req-filter]', host).forEach(function (b) { b.classList.toggle('is-active', b === btn); });
      renderRequests();
    });
  }

  function renderRequests() {
    var body = $('#cust-requests-body');
    if (!body) return;
    var rows = myRows().filter(function (p) { return reqFilter === 'All' || p.status === reqFilter; });
    if (!rows.length) { body.innerHTML = '<tr><td colspan="7" class="es-empty">No requests in this view.</td></tr>'; return; }
    body.innerHTML = rows.map(function (p) {
      var cancellable = p.status === 'Scheduled';
      return '<tr data-req-row="' + p.id + '">' +
        '<td class="font-medium text-gray-900 dark:text-gray-100">' + p.id + '</td>' +
        '<td>' + p.category + '</td>' +
        '<td>' + formatDate(p.date) + ' · ' + p.slot + '</td>' +
        '<td>' + (p.verified || p.weight) + ' kg</td>' +
        '<td class="font-semibold text-primary dark:text-primaryLight">' + (p.amount ? money(p.amount) : '—') + '</td>' +
        '<td>' + statusBadge(p.status) + '</td>' +
        '<td class="text-end whitespace-nowrap">' +
        (cancellable ? '<button type="button" class="es-btn es-btn--ghost es-btn--sm" data-cancel-req="' + p.id + '">Cancel</button>' : '') +
        '<button type="button" class="es-btn es-btn--ghost es-btn--sm ms-1" data-req-view="' + p.id + '">View</button>' +
        '</td></tr>';
    }).join('');
  }

  function renderWeights() {
    // chart
    var chart = $('#cust-weight-chart');
    var pickups = myRows().filter(function (p) { return Number(p.verified) || Number(p.weight); });
    if (chart) {
      var months = [];
      var base = new Date();
      for (var i = 5; i >= 0; i--) {
        var d = new Date(base.getFullYear(), base.getMonth() - i, 1);
        months.push({ key: d.toISOString().slice(0, 7), label: d.toLocaleDateString('en-IN', { month: 'short' }) });
      }
      var totals = {};
      var max = 1;
      pickups.forEach(function (p) {
        var k = monthKey(p.date);
        var w = Number(p.verified) || Number(p.weight) || 0;
        totals[k] = (totals[k] || 0) + w;
      });
      months.forEach(function (m) { max = Math.max(max, totals[m.key] || 0); });
      // give demo shape if data is sparse
      if (Object.keys(totals).length < 2) {
        months.forEach(function (m, idx) { totals[m.key] = [22, 31, 18, 40, 27, 34][idx]; });
        max = 40;
      }
      chart.innerHTML = months.map(function (m) {
        var v = totals[m.key] || 0;
        var h = Math.max(4, Math.round((v / max) * 100));
        return '<div class="es-bar__col" title="' + v.toFixed(1) + ' kg"><div class="es-bar__fill" style="height:' + h + '%"></div><span class="text-xs text-gray-500 dark:text-gray-400">' + m.label + '</span></div>';
      }).join('');
    }
    // category split
    var split = $('#cust-category-split');
    if (split) {
      var byCat = {};
      var total = 0;
      pickups.forEach(function (p) {
        var w = Number(p.verified) || Number(p.weight) || 0;
        byCat[p.category] = (byCat[p.category] || 0) + w;
        total += w;
      });
      if (!total) { byCat = { 'Paper & Cardboard': 30, 'Metal & Aluminum': 22, 'E-Waste': 14, 'Plastic & Packaging': 20, 'Old Appliances': 14 }; total = 100; }
      split.innerHTML = Object.keys(byCat).map(function (c) {
        var pct = Math.round((byCat[c] / total) * 100);
        return '<div><div class="flex justify-between text-sm mb-1"><span class="text-gray-600 dark:text-gray-300">' + c + '</span><span class="font-semibold text-gray-900 dark:text-white">' + byCat[c].toFixed(1) + ' kg · ' + pct + '%</span></div><div class="es-progress"><span class="es-progress__fill block" style="width:' + pct + '%"></span></div></div>';
      }).join('');
    }
    // ledger
    var body = $('#cust-weights-body');
    if (body) {
      body.innerHTML = pickups.slice().reverse().map(function (p) {
        var w = Number(p.verified) || Number(p.weight) || 0;
        return '<tr><td>' + formatDate(p.date) + '</td><td>' + p.category + '</td><td>' + w.toFixed(1) + ' kg</td><td>₹' + p.rate + '/' + (p.unit || 'kg') + '</td><td class="font-semibold text-primary dark:text-primaryLight">' + (p.amount ? money(p.amount) : '—') + '</td></tr>';
      }).join('') || '<tr><td colspan="5" class="es-empty">No weights recorded yet.</td></tr>';
    }
  }

  function renderPayouts() {
    var done = myRows().filter(function (p) { return p.status === 'Completed'; });
    var total = done.reduce(function (a, p) { return a + (Number(p.amount) || 0); }, 0);
    var pending = myRows().filter(function (p) { return p.status !== 'Completed' && p.status !== 'Cancelled'; }).reduce(function (a, p) { return a + (Number(p.verified) || Number(p.weight) || 0) * p.rate; }, 0);
    var avg = done.length ? total / done.length : 0;
    var map = { 'pay-total': money(total), 'pay-pending': money(pending), 'pay-avg': money(avg) };
    Object.keys(map).forEach(function (k) { $$('[data-stat="' + k + '"]').forEach(function (e) { e.textContent = map[k]; }); });

    var body = $('#cust-payouts-body');
    if (body) {
      body.innerHTML = done.slice().reverse().map(function (p) {
        return '<tr><td>' + formatDate(p.date) + '</td><td class="font-medium text-gray-900 dark:text-gray-100">' + p.id + '</td><td><span class="es-badge es-badge--slate">' + p.method + '</span></td><td>' + (p.verified || p.weight) + ' kg</td><td class="font-semibold text-primary dark:text-primaryLight">' + money(p.amount) + '</td><td>' + statusBadge('Completed') + '</td></tr>';
      }).join('') || '<tr><td colspan="6" class="es-empty">No payouts yet.</td></tr>';
    }
  }

  function renderAddresses() {
    seedAddresses();
    var host = $('#cust-address-list');
    if (!host) return;
    var list = Store.get('addresses', []);
    host.innerHTML = '<div class="grid sm:grid-cols-2 gap-4">' + list.map(function (a) {
      return '<div class="es-card"><div class="es-card__body">' +
        '<div class="flex items-center justify-between gap-2"><span class="es-badge es-badge--green"><i class="fa-solid fa-location-dot"></i> ' + a.label + (a.primary ? ' · Primary' : '') + '</span>' +
        '<button type="button" class="text-gray-400 hover:text-red-500" data-del-address="' + a.id + '" aria-label="Remove address"><i class="fa-solid fa-trash-can"></i></button></div>' +
        '<p class="es-card__text mt-3">' + a.address + '</p>' +
        '<p class="text-xs text-gray-400"><i class="fa-solid fa-city me-1"></i>' + a.city + '</p>' +
        '</div></div>';
    }).join('') + '</div>';
  }

  function renderNotifs() {
    var host = $('#cust-notif-list');
    if (!host) return;
    var list = seedNotifs();
    host.innerHTML = list.map(function (n) {
      return '<div class="flex items-start gap-3 p-4' + (n.read ? ' opacity-60' : '') + '">' +
        '<span class="w-9 h-9 rounded-full bg-primary/10 text-primary flex items-center justify-center flex-none"><i class="fa-solid ' + n.icon + '"></i></span>' +
        '<div class="flex-1"><p class="text-sm font-semibold text-gray-900 dark:text-white">' + n.title + '</p><p class="text-xs text-gray-500 dark:text-gray-400 mt-0.5">' + n.time + '</p></div>' +
        (n.read ? '' : '<span class="w-2 h-2 rounded-full bg-primary mt-2"></span>') +
        '</div>';
    }).join('');
    var unread = list.filter(function (n) { return !n.read; }).length;
    $$('[data-notif-badge]').forEach(function (b) { b.textContent = String(unread); b.style.display = unread ? '' : 'none'; });
  }

  function renderTracker() {
    var rows = myRows();
    var active = rows.filter(function (p) { return p.status === 'En Route'; })[0] || rows.filter(function (p) { return p.status === 'Scheduled'; })[0];
    var badge = $('[data-tracker-badge]');
    if (!active) {
      var req = $('#tracker-req');
      if (req) req.textContent = 'No active pickup';
      if (badge) { badge.className = 'es-badge es-badge--slate'; badge.innerHTML = '<i class="fa-solid fa-circle-info"></i> Idle'; }
      return;
    }
    var reqEl = $('#tracker-req');
    if (reqEl) reqEl.textContent = 'Request #' + active.id + ' · ' + active.category;
    if (badge) {
      var m = STATUS_META[active.status] || STATUS_META['Scheduled'];
      badge.className = 'es-badge es-badge--' + m.cls;
      badge.innerHTML = '<i class="fa-solid ' + m.icon + '"></i> ' + active.status;
    }
    var current = active.status === 'En Route' ? 2 : 1;
    $$('.es-stepper__step').forEach(function (step, i) {
      step.classList.toggle('is-done', i < current);
      step.classList.toggle('is-current', i === current);
    });
    var progress = [0, 20, 40, 64, 82, 100][current + 1] || 40;
    var bar = $('[data-dash-view="status"] .es-progress__fill');
    if (bar) bar.style.width = progress + '%';
  }

  function renderPayment() {
    var p = Store.get('payment', { method: 'UPI', upi: 'greenuser@upi', phone: '+91 98100 11223' });
    var form = $('#payment-form');
    if (!form) return;
    $$('input[name="method"]', form).forEach(function (r) { r.checked = r.value === p.method; });
    if ($('#pay-upi', form)) $('#pay-upi', form).value = p.upi || '';
    if ($('#pay-phone', form)) $('#pay-phone', form).value = p.phone || '';
  }

  function renderProfile() {
    var p = getProfile();
    if ($('#pf-name')) $('#pf-name').value = p.name;
    if ($('#pf-email')) $('#pf-email').value = p.email;
    if ($('#pf-phone')) $('#pf-phone').value = p.phone;
    // sign-up no longer asks for a city, so only override when one was saved
    if ($('#pf-city') && p.city) $('#pf-city').value = p.city;
  }

  /* ---------- navigation ---------- */
  var VIEW_TITLES = {
    overview: 'Dashboard', schedule: 'Schedule Pickup', requests: 'My Requests', status: 'Live Status',
    weights: 'Weight History', payouts: 'Payout History', payment: 'Payment Preferences',
    addresses: 'Saved Addresses', notifications: 'Notifications', profile: 'Profile Settings'
  };
  function navigate(key) {
    var view = $('[data-dash-view="' + key + '"]');
    if (!view) return;
    $$('[data-dash-view]').forEach(function (v) { v.classList.toggle('is-active', v === view); });
    $$('[data-dash-nav]').forEach(function (b) {
      if (b.tagName !== 'A') b.classList.toggle('is-active', b.getAttribute('data-dash-nav') === key);
    });
    var title = $('#dash-title');
    if (title) title.textContent = VIEW_TITLES[key] || 'Dashboard';
    if (window.location.hash.slice(1) !== key) history.replaceState(null, '', '#' + key);
    closeSidebar();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function openSidebar() { var s = $('#dash-sidebar'); if (s) s.classList.add('is-open'); var b = $('#dash-backdrop'); if (b) b.classList.add('is-open'); }
  function closeSidebar() { var s = $('#dash-sidebar'); if (s) s.classList.remove('is-open'); var b = $('#dash-backdrop'); if (b) b.classList.remove('is-open'); }

  function initNav() {
    $$('[data-dash-nav]').forEach(function (btn) {
      btn.addEventListener('click', function () { navigate(btn.getAttribute('data-dash-nav')); });
    });
    var burger = $('#dash-burger'); if (burger) burger.addEventListener('click', openSidebar);
    var close = $('#dash-close'); if (close) close.addEventListener('click', closeSidebar);
    var backdrop = $('#dash-backdrop'); if (backdrop) backdrop.addEventListener('click', closeSidebar);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSidebar(); });
    window.addEventListener('resize', function () { if (window.innerWidth >= 1024) closeSidebar(); });
    var hash = window.location.hash.slice(1);
    navigate(VIEW_TITLES[hash] ? hash : 'overview');
  }

  /* ---------- forms & actions ---------- */
  function initSchedule() {
    var form = $('#schedule-form');
    if (!form) return;
    var dateInput = $('#sc-date', form);
    if (dateInput) { dateInput.min = todayISO(); if (!dateInput.value) dateInput.value = todayISO(); }

    var weight = $('#sc-weight', form);
    var est = $('#est-value');
    function rateFor(cat) {
      if (cat.indexOf('Paper') === 0) return 14;
      if (cat.indexOf('Metal') === 0) return 28;
      if (cat.indexOf('Plastic') === 0) return 12;
      if (cat.indexOf('E-Waste') === 0) return 45;
      if (cat.indexOf('Old Appliance') === 0) return 650;
      if (cat.indexOf('Batter') === 0) return 180;
      return 18;
    }
    function updateEstimate() {
      if (!est || !weight) return;
      est.textContent = money((Number(weight.value) || 0) * rateFor($('#sc-cat', form).value));
    }
    if (weight) weight.addEventListener('input', updateEstimate);
    if ($('#sc-cat', form)) $('#sc-cat', form).addEventListener('change', updateEstimate);
    updateEstimate();

    form._onValid = function (data) {
      var pickups = seedPickups();
      var id = 'REQ-' + (1050 + pickups.length + 1);
      var profile = getProfile();
      var category = data.get('category');
      var rate = rateFor(category);
      pickups.unshift({
        id: id, customer: profile.name, email: profile.email,
        category: category, material: category, date: data.get('date'), slot: data.get('slot'),
        city: data.get('city'), address: data.get('address'), notes: data.get('notes') || '',
        weight: Number(data.get('weight')) || 0, verified: 0, rate: rate, amount: 0,
        status: 'Scheduled', method: Store.get('payment', { method: 'UPI' }).method || 'UPI'
      });
      Store.set('pickups', pickups);
      if (window.EcoForms) window.EcoForms.alert(form, '');
      toast('Pickup ' + id + ' scheduled for ' + formatDate(data.get('date')) + '.', 'success');
      form.reset();
      if (dateInput) dateInput.value = todayISO();
      refresh();
      navigate('requests');
    };
  }

  function initRequestActions() {
    document.addEventListener('click', function (e) {
      var cancel = e.target.closest('[data-cancel-req]');
      if (cancel) {
        var id = cancel.getAttribute('data-cancel-req');
        var pickups = seedPickups();
        var row = pickups.filter(function (p) { return p.id === id; })[0];
        if (row) { row.status = 'Cancelled'; Store.set('pickups', pickups); toast('Request ' + id + ' cancelled.', 'info'); refresh(); }
        return;
      }
      var view = e.target.closest('[data-req-view]');
      if (view) {
        var vid = view.getAttribute('data-req-view');
        var p = seedPickups().filter(function (x) { return x.id === vid; })[0];
        if (p) toast(p.id + ' · ' + p.category + ' · ' + (p.verified || p.weight) + ' kg · ' + p.status, 'info');
      }
    });
  }

  function initPayment() {
    var form = $('#payment-form');
    if (!form) return;
    form._onValid = function (data) {
      var methodEl = $('input[name="method"]:checked', form);
      Store.set('payment', {
        method: methodEl ? methodEl.value : 'UPI',
        upi: data.get('upi') || '',
        phone: data.get('phone') || ''
      });
      if (window.EcoForms) window.EcoForms.alert(form, '');
      toast('Payment preferences saved.', 'success');
    };
  }

  function initAddresses() {
    var form = $('#address-form');
    if (form) {
      form._onValid = function (data) {
        var list = Store.get('addresses', []);
        list.push({ id: 'ad-' + Date.now(), label: data.get('label'), city: data.get('city'), address: data.get('address'), primary: false });
        Store.set('addresses', list);
        if (window.EcoForms) window.EcoForms.alert(form, '');
        toast('Address saved.', 'success');
        form.reset();
        renderAddresses();
      };
    }
    document.addEventListener('click', function (e) {
      var del = e.target.closest('[data-del-address]');
      if (!del) return;
      var id = del.getAttribute('data-del-address');
      Store.set('addresses', Store.get('addresses', []).filter(function (a) { return a.id !== id; }));
      toast('Address removed.', 'info');
      renderAddresses();
    });
  }

  function initNotifs() {
    var clear = $('[data-clear-notifs]');
    if (clear) {
      clear.addEventListener('click', function () {
        var list = seedNotifs().map(function (n) { n.read = true; return n; });
        Store.set('notifs', list);
        toast('All notifications marked as read.', 'success');
        renderNotifs();
      });
    }
  }

  function initProfile() {
    var form = $('#profile-form');
    if (!form) return;
    form._onValid = function (data) {
      var profile = { name: data.get('name'), email: data.get('email'), phone: data.get('phone'), city: data.get('city') };
      Store.set('profile', profile);
      if (window.EcoForms) window.EcoForms.alert(form, '');
      toast('Profile updated.', 'success');
      paintUser();
    };
  }

  function initDemo() {
    $$('[data-demo-action]').forEach(function (btn) {
      btn.addEventListener('click', function () { toast(btn.getAttribute('data-demo-action') + ' is a demo action.', 'info'); });
    });
    $$('[data-dash-logout]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        Auth.logout();
        toast('Logged out. See you soon!', 'info');
        window.setTimeout(function () { window.location.href = 'login.html'; }, 600);
      });
    });
  }

  /* ---------- refresh ---------- */
  function refresh() {
    renderStats();
    renderRecent();
    renderRequests();
    renderWeights();
    renderPayouts();
    renderTracker();
    renderAddresses();
    renderNotifs();
    renderPayment();
    renderProfile();
  }

  function init() {
    paintUser();
    renderRequestFilters();
    initNav();
    initSchedule();
    initRequestActions();
    initPayment();
    initAddresses();
    initNotifs();
    initProfile();
    initDemo();
    refresh();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
