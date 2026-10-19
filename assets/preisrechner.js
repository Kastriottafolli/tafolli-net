/* Unverbindliche Preisschätzung aus den veröffentlichten Endpreisen. Läuft nur im Browser. */
(function (root, factory) {
  var api = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', api.starten);
    else api.starten();
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  var STUFEN = { '99': 'Basis', '199': 'Laufend', '299': 'Intensiv' };
  var TEXTE = {
    dokument: [49, 'Dokument oder Prospekt'],
    website: [59, 'Website-Text'],
    content: [99, 'Content-Paket']
  };
  var RECHT = 'Endpreis. Gemäß § 19 UStG wird keine Umsatzsteuer berechnet.';

  function euro(n) {
    return new Intl.NumberFormat('de-DE', { maximumFractionDigits: 0 }).format(n) + ' €';
  }

  function einheit(prefix, auswahl, spanne) {
    var satz = prefix + ': Ihre Auswahl: ' + auswahl + '.';
    if (spanne) satz += ' Spanne: ' + spanne + '.';
    return satz + ' Unverbindlich.';
  }

  function schaetzung(s) {
    var lines = [];
    var leistung = s.leistung || 'website';
    if (leistung === 'ki') {
      lines.push('Einmalig: KI-Automatisierung: Festpreis auf Anfrage. Unverbindlich.');
    } else if (leistung === 'website') {
      lines.push('Einmalig: Website oder Landingpage: Festpreis auf Anfrage. Unverbindlich.');
      if (s.mitPflege) lines.push(pflegeZeile(s.pflege));
    } else if (leistung === 'shop') {
      var shop = s.shop === 'erweitert' ? 1990 : 990;
      var shopName = s.shop === 'erweitert' ? 'Erweitert' : 'Start';
      lines.push(einheit('Einmalig', euro(shop), '990–1.990 €').replace('Ihre Auswahl:', 'Onlineshop, Stufe ' + shopName + '. Ihre Auswahl:'));
    } else if (leistung === 'app') {
      var auswahl = s.app === 'gross' ? 'Festpreis nach Angebot' : 'ab 390 €';
      lines.push(einheit('Einmalig', auswahl, 'ab 390 €, größere Projekte nach Angebot').replace('Ihre Auswahl:', 'Web-App oder Tool. Ihre Auswahl:'));
    } else if (leistung === 'pflege') {
      lines.push(pflegeZeile(s.pflege));
    } else if (leistung === 'profile') {
      var komplett = s.profil === 'komplett';
      lines.push(einheit('Einmalig', euro(komplett ? 899 : 399), '399–899 €').replace('Ihre Auswahl:', 'Firmenprofile ' + (komplett ? 'Komplett' : 'Basis') + '. Ihre Auswahl:'));
    } else if (leistung === 'texte') {
      var paket = TEXTE[s.text] || TEXTE.dokument;
      var teile = [paket[1]];
      if (s.weitere) teile.push('weitere Sprache');
      if (s.eil) teile.push('Eilauftrag');
      var satz = 'Einmalig: ' + teile.join(', ') + '. Ihre Auswahl: ' + euro(paket[0]) + '. Spanne: 49–99 €.';
      if (s.weitere || s.eil) satz += ' Aufpreis nach Absprache.';
      lines.push(satz + ' Unverbindlich.');
    }
    return lines;
  }

  function pflegeZeile(wert) {
    var stufe = String(wert || '99');
    if (!STUFEN[stufe]) stufe = '99';
    return einheit('Monatlich', euro(Number(stufe)), '99–299 € pro Monat').replace('Ihre Auswahl:', 'Website-Pflege ' + STUFEN[stufe] + '. Ihre Auswahl:');
  }

  function mailto(lines) {
    var body = ['Unverbindliche Schätzung von tafolli.net', ''].concat(lines, [RECHT]).join('\r\n');
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

  function pflegeSchalter(form) {
    var selects = form.querySelectorAll('[data-pflege]');
    for (var i = 0; i < selects.length; i++) {
      var panel = selects[i].closest('[data-panel]');
      var box = panel && panel.querySelector('[data-mit-pflege]');
      selects[i].disabled = box ? !box.checked : false;
    }
  }

  function aktualisieren(form) {
    var leistung = wert(form, 'leistung') || 'website';
    var panels = form.querySelectorAll('[data-panel]');
    for (var i = 0; i < panels.length; i++) panels[i].hidden = panels[i].getAttribute('data-panel') !== leistung;
    pflegeSchalter(form);
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
