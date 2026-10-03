/* tafolli.net v2 — so wenig JavaScript wie moeglich.
   Die Bewegung liegt im CSS. Hier steht nur, was CSS nicht kann. */
(function () {
  'use strict';

  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var scrollDriven = window.CSS && CSS.supports && CSS.supports('animation-timeline', 'view()');

  /* ── Einblenden, nur als Ersatz ───────────────────────────────────
     Kann der Browser Scroll-Driven Animations, macht das CSS die
     Arbeit und hier passiert nichts. Sonst uebernimmt ein Observer. */
  var ziele = document.querySelectorAll('.rise, .pop, .wipe');
  if (ziele.length) {
    if (scrollDriven && !reduce) {
      /* CSS fuehrt. Nichts zu tun. */
    } else if ('IntersectionObserver' in window) {
      var offen = Array.prototype.slice.call(ziele);
      var zeigen = function (el) {
        el.classList.add('is-in');
        io.unobserve(el);
        var i = offen.indexOf(el);
        if (i > -1) offen.splice(i, 1);
      };
      /* Schwelle 0: ein schneller Wischer oder ein Ankersprung darf
         kein Element ueberspringen. Sonst bleibt es fuer immer weg. */
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) zeigen(e.target); });
      }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
      offen.forEach(function (el) { io.observe(el); });

      /* Fangnetz fuer alles, was die Auslinie schon passiert hat. */
      var geplant = false;
      var lauf = function () {
        geplant = false;
        for (var i = offen.length - 1; i >= 0; i--) {
          if (offen[i].getBoundingClientRect().top < innerHeight * 0.92) zeigen(offen[i]);
        }
        if (!offen.length) {
          removeEventListener('scroll', anstossen);
          removeEventListener('resize', anstossen);
        }
      };
      var anstossen = function () { if (!geplant) { geplant = true; requestAnimationFrame(lauf); } };
      addEventListener('scroll', anstossen, { passive: true });
      addEventListener('resize', anstossen, { passive: true });
      anstossen();
    } else {
      Array.prototype.forEach.call(ziele, function (el) { el.classList.add('is-in'); });
    }
  }

  /* ── Menue ───────────────────────────────────────────────────────── */
  var knopf = document.querySelector('.burger');
  var blatt = document.getElementById('sheet');
  if (knopf && blatt) {
    var offenJa = function () { return knopf.getAttribute('aria-expanded') === 'true'; };
    var setzen = function (auf) {
      knopf.setAttribute('aria-expanded', auf ? 'true' : 'false');
      if (auf) blatt.setAttribute('data-open', ''); else blatt.removeAttribute('data-open');
    };
    knopf.addEventListener('click', function (e) { e.stopPropagation(); setzen(!offenJa()); });
    blatt.addEventListener('click', function (e) { if (e.target.tagName === 'A') setzen(false); });
    document.addEventListener('click', function (e) {
      if (offenJa() && !blatt.contains(e.target) && e.target !== knopf) setzen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && offenJa()) { setzen(false); knopf.focus(); }
    });
    matchMedia('(min-width: 1041px)').addEventListener('change', function (e) { if (e.matches) setzen(false); });
  }

  /* ── Kennzahlen zaehlen hoch ─────────────────────────────────────── */
  var zahlen = document.querySelectorAll('[data-zaehl]');
  if (zahlen.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(zahlen, function (el) {
        el.textContent = el.getAttribute('data-zaehl') + (el.getAttribute('data-suffix') || '');
      });
    } else {
      var io2 = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          io2.unobserve(e.target);
          var el = e.target;
          var ziel = parseFloat(el.getAttribute('data-zaehl')) || 0;
          var suffix = el.getAttribute('data-suffix') || '';
          var t0 = null;
          requestAnimationFrame(function schritt(ts) {
            if (t0 === null) t0 = ts;
            var p = Math.min((ts - t0) / 1400, 1);
            el.textContent = Math.round((1 - Math.pow(1 - p, 3)) * ziel) + suffix;
            if (p < 1) requestAnimationFrame(schritt);
          });
        });
      }, { threshold: 0.35 });
      Array.prototype.forEach.call(zahlen, function (el) { io2.observe(el); });
    }
  }

  /* ── Terminal ────────────────────────────────────────────────────── */
  var term = document.getElementById('term');
  if (term) {
    var zeilen = Array.prototype.slice.call(term.querySelectorAll('[data-z]'));
    var texte = zeilen.map(function (z) { return z.textContent; });
    var cur = term.querySelector('.cursor');
    if (reduce) {
      zeilen.forEach(function (z, i) { z.textContent = texte[i]; z.style.opacity = '1'; });
    } else {
      zeilen.forEach(function (z) { z.style.opacity = '1'; });
      (function runde() {
        var n = 0;
        zeilen.forEach(function (z) { z.textContent = ''; });
        (function zeile() {
          if (n >= zeilen.length) { if (cur) term.appendChild(cur); return setTimeout(runde, 3400), undefined; }
          var el = zeilen[n], voll = texte[n], befehl = voll.charAt(0) === '$';
          if (!befehl) {            /* Ausgaben tippt niemand. */
            el.textContent = voll;
            if (cur) el.appendChild(cur);
            n++; return setTimeout(zeile, 150), undefined;
          }
          var k = 0;
          (function zeichen() {
            el.textContent = voll.slice(0, k);
            if (cur) el.appendChild(cur);
            if (k < voll.length) { k++; setTimeout(zeichen, 22 + Math.random() * 34); }
            else { n++; setTimeout(zeile, 300); }
          })();
        })();
      })();
    }
  }
})();
