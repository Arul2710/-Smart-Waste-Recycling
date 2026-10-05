/* ===========================================================
   EcoScrap — Global RTL / LTR direction support
   - Flips <html dir> and mirrors the whole layout
   - Every [data-rtl-toggle] button stays in sync
   - Persists to localStorage so direction follows the user
   =========================================================== */
(function () {
  'use strict';

  var STORAGE_KEY = 'ecoscrap-dir';
  var root = document.documentElement;

  function readStored() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
  }
  function store(value) {
    try { localStorage.setItem(STORAGE_KEY, value); } catch (e) { /* private mode */ }
  }

  function syncButtons(isRtl) {
    var buttons = document.querySelectorAll('[data-rtl-toggle]');
    for (var i = 0; i < buttons.length; i++) {
      var btn = buttons[i];
      btn.setAttribute('aria-pressed', isRtl ? 'true' : 'false');
      btn.setAttribute('title', isRtl ? 'Switch to left-to-right' : 'Switch to right-to-left');
      btn.setAttribute('aria-label', isRtl ? 'Switch to left-to-right' : 'Switch to right-to-left');
      btn.setAttribute('data-dir-state', isRtl ? 'rtl' : 'ltr');
      // The button is always labelled "RTL"; the current state is carried by
      // aria-pressed / the active styling, never by rewriting the wording.
      var label = btn.querySelector('[data-rtl-label]');
      if (label) label.textContent = 'RTL';
    }
  }

  function apply(isRtl, persist) {
    root.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
    root.setAttribute('lang', isRtl ? 'ar' : 'en');
    if (persist !== false) store(isRtl ? 'rtl' : 'ltr');
    syncButtons(isRtl);
    document.dispatchEvent(new CustomEvent('ecoscrap:dir', { detail: { rtl: isRtl } }));
  }

  function isRtl() { return root.getAttribute('dir') === 'rtl'; }
  function toggle() { apply(!isRtl()); }

  window.EcoDir = { apply: apply, toggle: toggle, isRtl: isRtl };

  // Apply immediately so the first paint is already in the right direction.
  apply(readStored() === 'rtl', false);

  function init() {
    var buttons = document.querySelectorAll('[data-rtl-toggle]');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener('click', function (e) {
        e.preventDefault();
        toggle();
      });
    }
    syncButtons(isRtl());
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
