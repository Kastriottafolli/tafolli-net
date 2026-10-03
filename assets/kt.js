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

  /* Kennzahlen laufen jetzt als reine CSS-Ziffernrollen (.odo), der
     Wert steht zur Bauzeit fest. Kein Hochzaehl-Skript mehr noetig. */

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

  /* ── Eigener Zeiger, magnetische Knoepfe, Terminal-Neigung ──────────
     Alles in einer Schleife, nur auf echten Zeigegeraeten und nur ohne
     Bewegungsreduzierung. .cur-on setzt erst, wenn die Schleife wirklich
     laeuft — ein JS-Fehler kann so nie einen unsichtbaren Zeiger
     hinterlassen. */
  var fein = matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (fein && !reduce) {
    document.documentElement.classList.add('cur-on');

    var punkt = document.createElement('div'); punkt.className = 'cur cur-dot';
    var ring = document.createElement('div'); ring.className = 'cur cur-ring';
    document.body.appendChild(punkt); document.body.appendChild(ring);

    var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my, ringGross = false;
    addEventListener('mousemove', function (e) { mx = e.clientX; my = e.clientY; }, { passive: true });
    document.addEventListener('mouseover', function (e) {
      ringGross = !!(e.target.closest && e.target.closest('a, button, .lnk, .card'));
    }, { passive: true });

    (function schleife() {
      rx += (mx - rx) * .18; ry += (my - ry) * .18;
      punkt.style.transform = 'translate3d(' + mx + 'px,' + my + 'px,0) translate(-50%,-50%)';
      ring.style.transform = 'translate3d(' + rx + 'px,' + ry + 'px,0) translate(-50%,-50%)' + (ringGross ? ' scale(1.76)' : '');
      if (ringGross) ring.setAttribute('data-big', ''); else ring.removeAttribute('data-big');
      requestAnimationFrame(schleife);
    })();

    /* Magnetismus: Knopf folgt dem Zeiger innerhalb seiner Flaeche und
       federt beim Verlassen per CSS-Transition zurueck. Druckgefuehl
       sitzt direkt im selben Transform, weil eine CSS-:active-Regel vom
       laufenden Inline-Stil uebertoent wuerde. */
    Array.prototype.forEach.call(document.querySelectorAll('.btn'), function (m) {
      var dx = 0, dy = 0, gedrueckt = false;
      var zeichnen = function () {
        m.style.transform = 'translate3d(' + dx.toFixed(1) + 'px,' + dy.toFixed(1) + 'px,0)' + (gedrueckt ? ' scale(.97)' : '');
      };
      m.addEventListener('mousemove', function (e) {
        var r = m.getBoundingClientRect();
        dx = (e.clientX - (r.left + r.width / 2)) * .28;
        dy = (e.clientY - (r.top + r.height / 2)) * .28 - 2;
        zeichnen();
      });
      m.addEventListener('mousedown', function () { gedrueckt = true; zeichnen(); });
      m.addEventListener('mouseup', function () { gedrueckt = false; zeichnen(); });
      m.addEventListener('mouseleave', function () { gedrueckt = false; dx = 0; dy = 0; m.style.transform = ''; });
    });

    /* Das Terminal im Hero neigt sich zum Zeiger. Das einzige Objekt mit
       echter Zeiger-Antwort — die Karten darunter leben vom Scrollen,
       nicht vom Cursor, sonst wirkt jede Flaeche gleich laut. */
    var bruecke = document.querySelector('.pop-wrap');
    var innen = document.querySelector('.pop-wrap .tilt');
    if (bruecke && innen) {
      bruecke.addEventListener('mousemove', function (e) {
        var r = bruecke.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - .5, py = (e.clientY - r.top) / r.height - .5;
        innen.style.transform = 'rotateY(' + (px * 7).toFixed(2) + 'deg) rotateX(' + (-py * 7).toFixed(2) + 'deg)';
      });
      bruecke.addEventListener('mouseleave', function () { innen.style.transform = ''; });
    }
  }
})();
