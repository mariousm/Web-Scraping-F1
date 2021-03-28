# IMPORTS
from scraper import Scraper
from csvmodule import Csvmodule
import os

# Creamos el scraper y lo ejectuamos
scraper = Scraper()
data = scraper.__scraping__()

# Guardamos a un fichero CSV
fileName = "f1_dataset.csv"
path = os.path.join("data")

csv = Csvmodule(path, fileName, data, columnsName=["RACE", "DATE", "NATIONALITY_WINNER", "WINNER", "NATIONALITY_TEAM", "TEAM", "LAPS", "TIME", "TIME_PER_LAP"])
csv.__writeCsv__()