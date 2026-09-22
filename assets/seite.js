// Kastriot Tafolli, tafolli.net
(function () {
  'use strict';

  // Abschnitte blenden beim Scrollen ein
  var rev = document.querySelectorAll('.kt-reveal');
  if (rev.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('kt-visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    Array.prototype.forEach.call(rev, function (el) { io.observe(el); });
  } else {
    Array.prototype.forEach.call(rev, function (el) { el.classList.add('kt-visible'); });
  }

  // Kopfzeile und Fortschrittsbalken
  var nav = document.querySelector('.kt-navbar');
  var prog = document.querySelector('.kt-prog');
  function onScroll() {
    if (nav) nav.classList.toggle('kt-shrink', window.scrollY > 30);
    if (prog) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      prog.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Kennzahlen zählen hoch
  var cs = document.querySelectorAll('.kt-countup');
  if (cs.length && 'IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        io2.unobserve(e.target);
        var el = e.target;
        var tgt = parseFloat(el.getAttribute('data-target') || '0');
        var sfx = el.getAttribute('data-suffix') || '';
        var t0 = null;
        function step(ts) {
          if (t0 === null) t0 = ts;
          var p = Math.min((ts - t0) / 1600, 1);
          el.textContent = Math.round((1 - Math.pow(1 - p, 3)) * tgt) + sfx;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.4 });
    Array.prototype.forEach.call(cs, function (el) { io2.observe(el); });
  }

  // Terminal: Befehle werden Zeichen für Zeichen getippt, Ausgaben erscheinen
  // sofort danach, so wie in einer echten Shell. Läuft danach in Schleife.
  var term = document.getElementById('kt-term');
  if (term) {
    var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var lineEls = Array.prototype.slice.call(term.querySelectorAll('[data-line]'));
    var cursorEl = term.querySelector('.kt-cursor');
    var lineTexts = lineEls.map(function (l) { return l.textContent; });

    if (reduceMotion) {
      // Bewegungsreduzierung gewünscht: Text bleibt einfach vollständig sichtbar.
      lineEls.forEach(function (l, idx) { l.textContent = lineTexts[idx]; l.style.opacity = '1'; });
    } else {
      lineEls.forEach(function (l) { l.style.opacity = '1'; });

      var typeCycle = function () {
        var li = 0;
        lineEls.forEach(function (l) { l.textContent = ''; });

        var typeLine = function () {
          if (li >= lineEls.length) {
            if (cursorEl) term.appendChild(cursorEl);
            setTimeout(typeCycle, 2800);
            return;
          }
          var el = lineEls[li];
          var full = lineTexts[li];
          var isCommand = full.charAt(0) === '$';

          if (!isCommand) {
            // Ausgaben werden vom Terminal ausgegeben, nicht vom Nutzer getippt.
            el.textContent = full;
            if (cursorEl) el.appendChild(cursorEl);
            li += 1;
            setTimeout(typeLine, 140);
            return;
          }

          var ci = 0;
          var typeChar = function () {
            el.textContent = full.slice(0, ci);
            if (cursorEl) el.appendChild(cursorEl);
            if (ci < full.length) {
              ci += 1;
              setTimeout(typeChar, 24 + Math.random() * 36);
            } else {
              li += 1;
              setTimeout(typeLine, 280);
            }
          };
          typeChar();
        };
        typeLine();
      };
      typeCycle();
    }
  }

  // Rechner
  var calc = document.querySelector('input[data-in]') ? document : null;
  if (calc) {
    var s = {};
    var inputs = calc.querySelectorAll('input[data-in]');
    Array.prototype.forEach.call(inputs, function (el) {
      s[el.getAttribute('data-in')] = Number(el.value);
      el.addEventListener('input', function () {
        s[el.getAttribute('data-in')] = Number(el.value);
        render();
      });
    });

    function n0(v) { return Math.round(v).toLocaleString('de-DE'); }
    function eur(v) { return Math.round(v).toLocaleString('de-DE') + ' \u20AC'; }
    function pct(v) { return Math.max(0, Math.min(100, v)).toFixed(1) + '%'; }

    function render() {
      var kiMinTag = (s.anrufe + s.nachrichten) * s.minuten;
      var kiStdMonat = kiMinTag * 30 / 60;
      var kiStdGespart = kiStdMonat * 0.7;
      var kiJahrEur = kiStdGespart * s.lohn * 12;

      var umsatzMonat = s.naechte * s.preis;
      var portalUmsatzJahr = umsatzMonat * (s.portal / 100) * 12;
      var provJahrEur = portalUmsatzJahr * (s.prov / 100);
      var verschobenJahr = umsatzMonat * 12 * (Math.min(s.shift, s.portal) / 100);
      var sparenJahr = verschobenJahr * (s.prov / 100);
      var provNachher = Math.max(0, provJahrEur - sparenJahr);

      var rvHeuteEur = s.einkauf * (s.aktuell / 100);
      var rvZielEur = s.einkauf * (Math.max(s.ziel, s.aktuell) / 100);
      var rvPlusEur = rvZielEur - rvHeuteEur;
      var rvMax = Math.max(rvZielEur, 1);

      var postsMonat = s.posts * 4.33;
      var erPct = s.erate / 10;
      var imprMonat = postsMonat * s.follower * (0.35 + erPct / 100 * 2.2);
      var anfragen = imprMonat * 0.04 * 0.03;

      var v = {
        anrufe: s.anrufe, nachrichten: s.nachrichten, minuten: s.minuten, lohn: s.lohn,
        kiStunden: n0(kiStdMonat) + ' Std.', kiJahr: eur(kiJahrEur),
        kiBar1Txt: n0(kiStdMonat) + ' Std.', kiBar2Txt: n0(kiStdMonat - kiStdGespart) + ' Std.',
        naechte: s.naechte, preis: s.preis, portal: s.portal, prov: s.prov, shift: s.shift,
        provJahr: eur(provJahrEur), direktJahr: eur(sparenJahr),
        dBar1Txt: eur(provJahrEur), dBar2Txt: eur(provNachher),
        einkauf: s.einkauf, einkaufTxt: n0(s.einkauf), aktuell: s.aktuell, ziel: s.ziel,
        rvHeute: eur(rvHeuteEur), rvPlus: eur(rvPlusEur),
        rBar1Txt: eur(rvHeuteEur), rBar2Txt: eur(rvZielEur),
        posts: s.posts, follower: s.follower, followerTxt: n0(s.follower),
        erate: s.erate, erateTxt: erPct.toFixed(1),
        smImpr: n0(imprMonat), smAnfragen: n0(anfragen)
      };
      var bars = {
        kiBar1: '100%',
        kiBar2: pct(kiStdMonat > 0 ? (kiStdMonat - kiStdGespart) / kiStdMonat * 100 : 0),
        dBar1: '100%',
        dBar2: pct(provJahrEur > 0 ? provNachher / provJahrEur * 100 : 0),
        rBar1: pct(rvHeuteEur / rvMax * 100),
        rBar2: '100%'
      };

      Array.prototype.forEach.call(calc.querySelectorAll('[data-v]'), function (el) {
        var k = el.getAttribute('data-v');
        if (v[k] !== undefined) el.textContent = v[k];
      });
      Array.prototype.forEach.call(calc.querySelectorAll('[data-bar]'), function (el) {
        var k = el.getAttribute('data-bar');
        if (bars[k] !== undefined) el.style.width = bars[k];
      });
    }
    render();
  }
})();
