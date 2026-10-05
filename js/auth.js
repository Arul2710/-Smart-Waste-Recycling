/* ===========================================================
   EcoScrap — demo authentication
   Pure front-end: credentials are never sent anywhere. A demo
   session is stored in localStorage and powers the account menus
   in the navbar. Sessions carry a token, an absolute expiry and an
   inactivity window. Forms use EcoForms (js/main.js).
   The dashboards themselves are open to everyone and need no session.
   =========================================================== */
(function () {
  'use strict';

  var SESSION_KEY = 'ecoscrap-session';
  var USERS_KEY = 'ecoscrap-users';
  var VERSION = 2;
  var HOUR = 60 * 60 * 1000;
  var MAX_AGE = 12 * HOUR;
  var IDLE_LIMIT = 45 * 60 * 1000;
  var TOUCH_EVERY = 60 * 1000;

  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function read(key, fallback) {
    try { var raw = localStorage.getItem(key); return raw === null ? fallback : JSON.parse(raw); }
    catch (e) { return fallback; }
  }
  function write(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* ignore */ }
  }
  function drop(key) {
    try { localStorage.removeItem(key); } catch (e) { /* ignore */ }
  }
  function token() {
    var bytes = new Uint8Array(16);
    if (window.crypto && window.crypto.getRandomValues) window.crypto.getRandomValues(bytes);
    else for (var i = 0; i < bytes.length; i++) bytes[i] = Math.floor(Math.random() * 256);
    var out = '';
    for (var j = 0; j < bytes.length; j++) out += ('0' + bytes[j].toString(16)).slice(-2);
    return out;
  }

  function toast(message, type) {
    if (typeof window.EcoToast === 'function') return window.EcoToast(message, type);
    var box = $('[data-form-alert]');
    if (box) { box.className = 'es-alert es-alert--' + (type || 'success') + ' is-visible'; box.textContent = message; }
  }

  /* ---- session lifecycle --------------------------------------- */
  function isExpired(s) {
    if (!s || s.v !== VERSION) return false;
    var now = Date.now();
    if (s.expiresAt && now > Number(s.expiresAt)) return true;
    if (s.lastSeen && (now - Number(s.lastSeen)) > IDLE_LIMIT) return true;
    return false;
  }

  // Sessions written before the hardening pass carry no token/expiry; stamp
  // them once so an already signed-in visitor is not thrown out.
  function migrate(s) {
    if (!s || typeof s !== 'object') return null;
    var now = Date.now();
    s.v = VERSION;
    s.token = s.token || token();
    s.issuedAt = Number(s.issuedAt) || now;
    s.expiresAt = Number(s.expiresAt) || (now + MAX_AGE);
    s.lastSeen = now;
    write(SESSION_KEY, s);
    return s;
  }

  function current() {
    var s = read(SESSION_KEY, null);
    if (!s || typeof s !== 'object' || !s.role) { drop(SESSION_KEY); return null; }
    if (s.v !== VERSION) s = migrate(s);
    if (isExpired(s)) { drop(SESSION_KEY); return null; }
    return s;
  }

  // Sliding inactivity window, throttled so we are not writing on every event.
  function touch() {
    var s = current();
    if (!s) return null;
    if (Date.now() - Number(s.lastSeen || 0) > TOUCH_EVERY) {
      s.lastSeen = Date.now();
      write(SESSION_KEY, s);
    }
    return s;
  }

  var HOME = { customer: 'customer-dashboard.html', admin: 'admin-dashboard.html' };

  var Auth = {
    session: current,
    isLoggedIn: function () { return !!current(); },
    isAdmin: function () { var s = current(); return !!s && s.role === 'admin'; },
    hasRole: function (role) { var s = current(); return !!s && s.role === role; },
    touch: touch,
    login: function (user) {
      var now = Date.now();
      user.since = new Date().toISOString();
      user.v = VERSION;
      user.token = token();
      user.issuedAt = now;
      user.expiresAt = now + MAX_AGE;
      user.lastSeen = now;
      user.idle = IDLE_LIMIT;
      user.maxAge = MAX_AGE;
      write(SESSION_KEY, user);
      return user;
    },
    logout: function () {
      drop(SESSION_KEY);
    },
    nameFromEmail: function (email) {
      var base = String(email || 'green guest').split('@')[0].replace(/[._-]+/g, ' ');
      return base.replace(/\b\w/g, function (c) { return c.toUpperCase(); }).trim() || 'Green Guest';
    },
    initials: function (name) {
      var parts = String(name || 'G G').trim().split(/\s+/);
      return ((parts[0] || 'G')[0] + (parts[1] ? parts[1][0] : '')).toUpperCase();
    }
  };
  window.EcoAuth = Auth;

  /* ---- show / hide password ------------------------------------ */
  function initPasswordToggles() {
    $$('[data-pw-toggle]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var input = document.getElementById(btn.getAttribute('data-pw-toggle'));
        if (!input) return;
        var show = input.type === 'password';
        input.type = show ? 'text' : 'password';
        var icon = $('i', btn);
        if (icon) { icon.classList.toggle('fa-eye', !show); icon.classList.toggle('fa-eye-slash', show); }
        btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
      });
    });
  }

  /* ---- demo social buttons ------------------------------------- */
  function initSocial() {
    $$('[data-social]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        toast(btn.getAttribute('data-social') + ' sign-in is disabled in this demo. Use the form below.', 'info');
      });
    });
  }

  /* ---- role on the login page ---------------------------------- */
  // The page no longer shows a Customer/Admin switcher, so the role is set
  // once from ?role= (default customer) into the hidden form field.
  function selectRole(role) {
    var hidden = $('#login-role');
    if (hidden) hidden.value = role;
  }

  // Supports ?role=admin&next=admin-dashboard.html so an admin sign-in link
  // can preselect the role for anyone following it.
  function requestedRole() {
    try {
      var role = (new URLSearchParams(window.location.search).get('role') || '').toLowerCase();
      return role === 'admin' ? 'admin' : 'customer';
    } catch (e) { return 'customer'; }
  }

  function initRoleTabs() {
    // The Customer/Admin switcher is no longer part of the page, so there is
    // nothing to click; the hidden field still follows ?role= so deep links to
    // the admin sign-in keep working.
    selectRole(requestedRole());
  }

  /* ---- where to send the user after login --------------------- */
  // Only a small allow-list of in-app pages may be used as a redirect
  // target, so ?next= can never be abused as an open redirect.
  function resolveTarget(role) {
    var fallback = HOME[role] || HOME.customer;
    try {
      var next = new URLSearchParams(window.location.search).get('next') || '';
      var allowed = next === HOME.customer || next === HOME.admin;
      if (allowed && next === HOME.admin && role !== 'admin') return fallback;
      return allowed ? next : fallback;
    } catch (e) {
      return fallback;
    }
  }

  function queryParam(name) {
    try { return new URLSearchParams(window.location.search).get(name) || ''; }
    catch (e) { return ''; }
  }

  function hasNext() {
    return !!queryParam('next');
  }

  /* ---- login --------------------------------------------------- */
  function initLogin() {
    var form = $('#login-form');
    if (!form) return;
    form._onValid = function (data) {
      var email = (data.get('email') || data.get('identifier') || '').trim();
      var role = (data.get('role') || 'customer').toLowerCase();
      var users = read(USERS_KEY, []);
      var found = users.filter(function (u) { return u.email && u.email.toLowerCase() === email.toLowerCase(); })[0];
      var user = {
        name: (found && found.name) || Auth.nameFromEmail(email),
        email: email,
        role: role === 'admin' ? 'admin' : 'customer'
      };
      Auth.login(user);
      if (EcoForms) EcoForms.alert(form, '');
      toast('Welcome back, ' + user.name + '! Redirecting to your ' + (user.role === 'admin' ? 'admin' : 'customer') + ' dashboard…', 'success');
      var target = resolveTarget(user.role);
      window.setTimeout(function () { window.location.href = target; }, 900);
    };
  }

  /* ---- signup -------------------------------------------------- */
  function initSignup() {
    var form = $('#signup-form');
    if (!form) return;
    form._onValid = function (data) {
      var user = {
        name: (data.get('name') || '').trim(),
        email: (data.get('email') || '').trim(),
        phone: (data.get('phone') || '').trim(),
        // Self-registration can only ever create a customer account; the admin
        // role is reserved for credentials issued outside this form.
        role: 'customer',
        created: new Date().toISOString().slice(0, 10)
      };
      var users = read(USERS_KEY, []);
      var exists = users.filter(function (u) { return u.email && u.email.toLowerCase() === user.email.toLowerCase(); })[0];
      if (exists) {
        if (EcoForms.alert) EcoForms.alert(form, 'An account with this email already exists. Try logging in instead.', 'error');
        toast('This email is already registered in the demo.', 'error');
        return;
      }
      users.push(user);
      write(USERS_KEY, users);
      Auth.login({ name: user.name, email: user.email, role: user.role });
      if (EcoForms.alert) EcoForms.alert(form, '');
      toast('Account created — welcome to EcoScrap, ' + user.name + '!', 'success');
      window.setTimeout(function () { window.location.href = resolveTarget(user.role); }, 900);
    };
  }

  /* ---- forgot password ----------------------------------------- */
  function initForgot() {
    var form = $('#forgot-form');
    if (!form) return;
    form._onValid = function (data) {
      var email = (data.get('email') || '').trim();
      if (!email) return;
      if (EcoForms.alert) {
        EcoForms.alert(form, 'Reset link sent! We have emailed a password-reset link to ' + email + '. (Demo only — no email is actually sent.)', 'success');
      }
      toast('Reset instructions sent to ' + email + ' (demo).', 'success');
      form.reset();
    };
  }

  function init() {
    initPasswordToggles();
    initSocial();
    initRoleTabs();
    initLogin();
    initSignup();
    initForgot();
    explainRedirect();
  }

  // Tell the visitor why they landed here (deep link, expired session).
  function explainRedirect() {
    var form = $('#login-form') || $('#signup-form');
    if (!form || !window.EcoForms) return;
    var reason = queryParam('reason');

    if (reason === 'expired') {
      window.EcoForms.alert(form, 'Your session expired after a period of inactivity. Please log in again.', 'info');
    } else if (requestedRole() === 'admin') {
      window.EcoForms.alert(form, 'You chose the Admin account. Sign in to manage the EcoScrap console.', 'info');
    } else if (hasNext()) {
      window.EcoForms.alert(form, 'Please log in to continue to that page.', 'info');
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
