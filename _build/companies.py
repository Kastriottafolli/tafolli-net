"""Official destinations for the named career stations."""
import html
COMPANIES=[
 ('Grand Hotel Binz','https://www.grandhotelbinz.com/de/'),
 ('Cerês am Meer','https://arosahotels.de/hotels/ceres-am-meer.html'),
 ('Rösing Touristik','https://www.roesing-touristik.de/'),
 ('Raulff-Hotels','https://www.raulff-hotels.de/'),
]
def company_link(text):
    for name,url in COMPANIES:
        if name in text:
            return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{html.escape(text)} <span aria-hidden="true">↗</span></a>'
    return html.escape(text)
