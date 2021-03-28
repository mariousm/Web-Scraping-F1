# IMPORTS
from scraper import Scraper

# Creamos el scraper y lo ejectuamos
scraper = Scraper()
data = scraper.__scraping__()
print(data)

# Guardamos a un fichero CSV