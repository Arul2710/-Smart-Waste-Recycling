/* ===========================================================
   EcoScrap — Global Dark Mode
   - Applies the stored theme as early as possible (no FOUC)
   - Every [data-theme-toggle] button on the page stays in sync
   - Persists to localStorage so the choice follows the user
   =========================================================== */
(function () {
  'use strict';

  var STORAGE_KEY = 'ecoscrap-theme';
  var root = document.documentElement;

  function readStored() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
  }
  function store(value) {
    try { localStorage.setItem(STORAGE_KEY, value); } catch (e) { /* private mode */ }
  }

  function systemPrefersDark() {
    return typeof window.matchMedia === 'function' &&
      window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function resolveInitial() {
    var stored = readStored();
    if (stored === 'dark') return true;
    if (stored === 'light') return false;
    return systemPrefersDark();
  }

  function syncButtons(isDark) {
    var buttons = document.querySelectorAll('[data-theme-toggle]');
    for (var i = 0; i < buttons.length; i++) {
      var btn = buttons[i];
      btn.setAttribute('aria-pressed', isDark ? 'true' : 'false');
      btn.setAttribute('title', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      btn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      btn.setAttribute('data-theme-state', isDark ? 'dark' : 'light');
      var moon = btn.querySelector('.fa-moon');
      var sun = btn.querySelector('.fa-sun');
      if (moon) moon.classList.toggle('hidden', isDark);
      if (sun) sun.classList.toggle('hidden', !isDark);
      var label = btn.querySelector('[data-theme-label]');
      if (label) label.textContent = isDark ? 'Light Mode' : 'Dark Mode';
    }
  }

  function apply(isDark, persist) {
    root.classList.toggle('dark', isDark);
    root.style.colorScheme = isDark ? 'dark' : 'light';
    if (persist !== false) store(isDark ? 'dark' : 'light');
    syncButtons(isDark);
    document.dispatchEvent(new CustomEvent('ecoscrap:theme', { detail: { dark: isDark } }));
  }

  function isDark() { return root.classList.contains('dark'); }
  function toggle() { apply(!isDark()); }

  // Expose a tiny public API used by the other scripts.
  window.EcoTheme = { apply: apply, toggle: toggle, isDark: isDark };

  // Apply immediately (script is loaded in <head> on purpose).
  apply(resolveInitial(), false);

  function bindButtons() {
    var buttons = document.querySelectorAll('[data-theme-toggle]');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener('click', function (e) {
        e.preventDefault();
        toggle();
      });
    }
  }

  function init() {
    bindButtons();
    syncButtons(isDark());

    // Follow the OS preference only while the user has not chosen explicitly.
    if (typeof window.matchMedia === 'function') {
      var mq = window.matchMedia('(prefers-color-scheme: dark)');
      var onChange = function (e) {
        if (!readStored()) apply(e.matches, false);
      };
      if (mq.addEventListener) mq.addEventListener('change', onChange);
      else if (mq.addListener) mq.addListener(onChange);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
