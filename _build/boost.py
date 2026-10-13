"""Localized homepage promotion for Tafolli Boost."""
from html import escape

COPY = {
    'de': {
        'label': 'TAFOLLI BOOST / BEWERBEN MIT KI',
        'heading': ['Deine Bewerbung.', 'Mit Tafolli Boost.'],
        'text': 'Aus deinem Lebenslauf und einer Stellenanzeige entstehen vier passende Bewerbungsdokumente. Boosty begleitet dich Schritt für Schritt – du prüfst die Angaben und entscheidest, was du verwendest.',
        'cta': 'Tafolli Boost entdecken',
        'link_label': 'Tafolli Boost entdecken (öffnet in einem neuen Tab)',
        'documents_label': 'EINE STELLE. VIER DOKUMENTE.',
        'documents': ['Lebenslauf', 'Anschreiben', 'Motivationsschreiben', 'Bewerbungs-E-Mail'],
        'note': 'Deutsch, Englisch und Albanisch. Alle Texte bleiben bearbeitbar.',
    },
    'en': {
        'label': 'TAFOLLI BOOST / APPLY WITH AI',
        'heading': ['Your application.', 'With Tafolli Boost.'],
        'text': 'Turn your CV and a job posting into four tailored application documents. Boosty guides you step by step – you check the details and decide what to use.',
        'cta': 'Discover Tafolli Boost',
        'link_label': 'Discover Tafolli Boost (opens in a new tab)',
        'documents_label': 'ONE ROLE. FOUR DOCUMENTS.',
        'documents': ['CV', 'Cover letter', 'Motivation letter', 'Application email'],
        'note': 'German, English and Albanian. Every text remains editable.',
    },
    'sq': {
        'label': 'TAFOLLI BOOST / APLIKO ME IA',
        'heading': ['Aplikimi yt.', 'Me Tafolli Boost.'],
        'text': 'Nga CV-ja jote dhe një shpallje pune krijohen katër dokumente aplikimi të përshtatura. Boosty të udhëzon hap pas hapi – ti kontrollon të dhënat dhe vendos çfarë do të përdorësh.',
        'cta': 'Zbulo Tafolli Boost',
        'link_label': 'Zbulo Tafolli Boost (hapet në një skedë të re)',
        'documents_label': 'NJË VEND PUNE. KATËR DOKUMENTE.',
        'documents': ['CV', 'Letër aplikimi', 'Letër motivimi', 'Email aplikimi'],
        'note': 'Gjermanisht, anglisht dhe shqip. Çdo tekst mund të redaktohet.',
    },
}


def promotion(language):
    copy = COPY[language]
    heading = '<br>'.join(escape(line) for line in copy['heading'])
    documents = ''.join(
        f'<li><span aria-hidden="true">0{i + 1}</span>{escape(document)}</li>'
        for i, document in enumerate(copy['documents'])
    )
    return f'''
<section class="x-boost x-section" id="tafolli-boost" aria-labelledby="boost-title">
 <div class="x-shell x-boost-grid">
  <div class="x-boost-copy">
   <p class="x-label">{escape(copy['label'])}</p>
   <h2 id="boost-title">{heading}</h2>
   <p>{escape(copy['text'])}</p>
   <div class="x-boost-actions">
    <a class="x-button x-button-lime" href="https://www.tafolliboost.com/" target="_blank" rel="noopener noreferrer" aria-label="{escape(copy['link_label'])}">{escape(copy['cta'])}<span aria-hidden="true">↗</span></a>
    <span class="x-label x-boost-domain">www.tafolliboost.com</span>
   </div>
  </div>
  <div class="x-boost-documents">
   <p class="x-label">{escape(copy['documents_label'])}</p>
   <ul>{documents}</ul>
   <p class="x-boost-note">{escape(copy['note'])}</p>
  </div>
 </div>
</section>'''
