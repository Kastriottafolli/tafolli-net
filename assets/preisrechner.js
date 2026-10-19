/* Unverbindliche Preisschätzung aus den veröffentlichten Endpreisen. Läuft nur im Browser. */
(function (root, factory) {
  var api = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', api.starten);
    else api.starten();
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  var STUFEN = { '99': 'Basis', '199': 'Laufend', '299': 'Eng' };
  var TEXTE = {
    dokument: [49, 35, 'Dokument oder Prospekt'],
    website: [59, 40, 'Website-Text'],
    content: [99, 79, 'Content-Paket']
  };

  function euro(n) {
    var s = String(Math.round(n));
    return s.replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ' €';
  }

  function schaetzung(s) {
    var lines = [];
    var leistung = s.leistung || 'website';
    if (leistung === 'website') {
      lines.push('Website oder Landingpage: Festpreis auf Anfrage');
      if (s.mitPflege) lines.push(pflegeZeile(s.pflege));
    } else if (leistung === 'shop') {
      var shop = s.shop === 'erweitert' ? 1990 : 990;
      var shopName = s.shop === 'erweitert' ? 'Erweitert' : 'Start';
      lines.push('Onlineshop ' + shopName + ': ' + euro(shop) + ' Festpreis (Spanne 990–1.990 €)');
    } else if (leistung === 'app') {
      if (s.app === 'gross') lines.push('Web-App oder Tool: Festpreis nach Angebot. Ein kleines Werkzeug beginnt bei 390 €.');
      else lines.push('Web-App oder Tool, kleines Werkzeug: ab 390 €');
    } else if (leistung === 'pflege') {
      lines.push(pflegeZeile(s.pflege));
    } else if (leistung === 'profile') {
      var komplett = s.profil === 'komplett';
      lines.push('Firmenprofile ' + (komplett ? 'Komplett' : 'Basis') + ': ' + euro(komplett ? 899 : 399) + ' Festpreis (Spanne 399–899 €)');
    } else if (leistung === 'texte') {
      var paket = TEXTE[s.text] || TEXTE.dokument;
      var summe = paket[0];
      var detail = paket[2] + ': ' + euro(paket[0]);
      if (s.weitere) {
        summe += paket[1];
        detail += ', weitere Sprache +' + euro(paket[1]);
      }
      if (s.eil) {
        summe = Math.round(summe * 1.3);
        detail += ', Eilauftrag +30 %';
      }
      lines.push(detail);
      lines.push('Geschätzt: ' + euro(summe));
    }
    lines.push('Unverbindliche Schätzung. Kein Angebot.');
    lines.push('Endpreis. Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.');
    return lines;
  }

  function pflegeZeile(wert) {
    var stufe = String(wert || '99');
    if (!STUFEN[stufe]) stufe = '99';
    return 'Website-Pflege ' + STUFEN[stufe] + ': ' + euro(Number(stufe)) + ' pro Monat, monatlich kündbar';
  }

  function mailto(lines) {
    var body = ['Unverbindliche Schätzung von tafolli.net', ''].concat(lines).join('\n');
    return 'mailto:info@tafolli.net?subject=' + encodeURIComponent('Preisschätzung von tafolli.net') + '&body=' + encodeURIComponent(body);
  }

  function wert(form, name) {
    var el = form.querySelector('[name="' + name + '"]:checked');
    return el ? el.value : '';
  }

  function lesen(form) {
    var leistung = wert(form, 'leistung') || 'website';
    var panel = form.querySelector('[data-panel="' + leistung + '"]');
    var pflege = panel && panel.querySelector('[data-pflege]');
    var mit = panel && panel.querySelector('[data-mit-pflege]');
    var weitere = panel && panel.querySelector('[data-weitere]');
    var eil = panel && panel.querySelector('[data-eil]');
    return {
      leistung: leistung,
      shop: wert(form, 'shop') || 'start',
      app: wert(form, 'app') || 'klein',
      pflege: pflege ? pflege.value : '99',
      mitPflege: !!(mit && mit.checked),
      profil: wert(form, 'profil') || 'basis',
      text: wert(form, 'text') || 'dokument',
      weitere: !!(weitere && weitere.checked),
      eil: !!(eil && eil.checked)
    };
  }

  function aktualisieren(form) {
    var leistung = wert(form, 'leistung') || 'website';
    var panels = form.querySelectorAll('[data-panel]');
    for (var i = 0; i < panels.length; i++) panels[i].hidden = panels[i].getAttribute('data-panel') !== leistung;
    var lines = schaetzung(lesen(form));
    var out = document.getElementById('preis-ergebnis');
    var mail = document.getElementById('preis-mail');
    if (out) out.textContent = lines.join('\n');
    if (mail) mail.setAttribute('href', mailto(lines));
  }

  function starten() {
    var form = document.getElementById('preisrechner');
    if (!form) return;
    form.addEventListener('submit', function (event) { event.preventDefault(); });
    form.addEventListener('change', function () { aktualisieren(form); });
    aktualisieren(form);
  }

  return { schaetzung: schaetzung, mailto: mailto, euro: euro, starten: starten };
});
