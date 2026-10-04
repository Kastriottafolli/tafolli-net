"""Career references: existing CV facts translated into customer benefits."""
import html
from partners import brand, logo

HOTELS=[
 dict(brand('hotel-schluchsee','Vier Jahreszeiten am Schluchsee','https://www.vjz.de/','Schwarzwald',True),
      period='seit 2026',role='F&B Manager',scope='5 F&B-Outlets · Resortbetrieb',
      experience='Im Wellness- und Familienresort verbinde ich die Abläufe von Restaurant, Café, Bar und Bankett. Fünf F&B-Outlets verlangen abgestimmte Teams, verlässliche Planung und einen Blick für das gesamte Gästeerlebnis.',
      benefit='Ich unterstütze Sie dabei, Ihre gastronomischen Angebote und Abläufe aufeinander abzustimmen – vom Frühstück bis zur Veranstaltung.'),
 dict(brand('hotel-raulff','Raulff-Hotels','https://www.raulff-hotels.de/','Rügen',True),
      period='2025',role='Gastronomischer Direktor',scope='267 Zimmer · 6 F&B-Outlets · Gruppenverantwortung',
      experience='Zwei Häuser mit 267 Zimmern und sechs F&B-Outlets sowie Verantwortung auf Gruppenebene: Hier gehörten Preisgestaltung, Einkauf und Lieferantenverhandlungen zu meinem Aufgabenbereich.',
      benefit='Sie erhalten einen wirtschaftlichen Blick auf Ihr F&B-Geschäft: von der Kalkulation über den Einkauf bis zu tragfähigen Lieferantenvereinbarungen.'),
 dict(brand('hotel-roesing','Rösing Touristik','https://www.roesing-touristik.de/','Rügen',True),
      period='2024',role='Director of Operations',scope='3 Hotels · 1 Resort · 5 Restaurants',
      experience='Drei Hotels und ein Resort mit fünf Restaurants: Meine operative Verantwortung umfasste die Vereinheitlichung von Standards, den Einkauf und die Personalplanung über mehrere Häuser hinweg.',
      benefit='Ich helfe Ihnen, Verantwortlichkeiten und Standards so zu strukturieren, dass Zusammenarbeit auch über mehrere Standorte hinweg funktioniert.'),
 dict(brand('hotel-binz','Vier Jahreszeiten Binz','https://www.vier-jahreszeiten.de/','Ostseebad Binz'),
      period='2023–2024',role='Gastronomischer Direktor / Director of Operations',scope='Vier Jahreszeiten · Meersinn · Suite Hotel',
      experience='Verantwortung für drei Hotels und sieben F&B-Outlets. Im Mittelpunkt standen gastronomische Konzepte, Qualitätssicherung und der Aufbau von Führungsstrukturen in den einzelnen Häusern.',
      benefit='Ich begleite Sie von der gastronomischen Idee bis zur Umsetzung: mit klaren Aufgaben, abgestimmten Qualitätsstandards und einem Konzept für den Betriebsalltag.'),
 dict(brand('hotel-ceres','Cerês am Meer','https://arosahotels.de/hotels/ceres-am-meer.html','Ostseebad Binz'),
      period='2022–2023',role='F&B Manager',scope='Designhotel · anspruchsvoller Service',note='Heute unter der Marke A-ROSA',
      experience='Im F&B-Management des Designhotels standen Servicequalität, präzise Abläufe und Aufmerksamkeit für Details im Mittelpunkt. Diese Erfahrung prägt meinen Anspruch an Gastfreundschaft und Teamführung.',
      benefit='Ich unterstütze Ihr Team dabei, hohen Serviceanspruch in klare Abläufe und eine verlässliche Qualität für Ihre Gäste zu übersetzen.'),
 dict(brand('hotel-grand-binz','Grand Hotel Binz','https://www.grandhotelbinz.com/de/','Ostseebad Binz',True),
      period='2018–2022',role='F&B Manager',scope='Restaurant · Bar · Frühstück · Room Service · Bankett',
      experience='Operative Verantwortung vom Frühstück bis zum Bankett: Neben den täglichen Abläufen gehörten Schulungskonzepte und die Ausbildung von Nachwuchskräften zu meiner Arbeit.',
      benefit='Sie profitieren von Erfahrung im gesamten Serviceablauf: mit praxistauglichen Standards, gezielter Einarbeitung und Schulungen für Ihr Team.'),
]

def hotel_cards():
    cards=[]
    for h in HOTELS:
        e=lambda key:html.escape(h[key])
        note=f'<span class="career-brand-note">{e("note")}</span>' if h.get('note') else ''
        cards.append(f'''<article class="career-card"><div class="career-card-top"><span>{e('field')}</span><span>{e('period')}</span></div><a class="career-brand-link" href="{e('url')}" target="_blank" rel="noopener noreferrer"><div class="career-logo-stage">{logo(h)}</div><h3>{e('name')}</h3>{note}<span class="career-website">Hotelwebsite ansehen <span aria-hidden="true">↗</span></span></a><p class="career-role">{e('role')}</p><p class="career-scope">{e('scope')}</p><p class="career-experience">{e('experience')}</p><div class="career-benefit"><h4>Ihr Mehrwert</h4><p>{e('benefit')}</p></div></article>''')
    return '<div class="career-grid">'+''.join(cards)+'</div>'
