# IMPORTS
import cloudscraper
from bs4 import BeautifulSoup

# Clase encarga de extraer los datos
class Scraper():

    # Constructor de la clase
    def __init__(self):
        self.url = "https://www.f1-fansite.com/f1-results/"
        self.data = []
        self.soup = None

    # Método que parsea el HTML a un objeto BeautifulSoup con el que navegar el DOM
    # https://stackoverflow.com/questions/49087990/python-request-being-blocked-by-cloudflare
    def __getHtml__(self, url):
        scraper = cloudscraper.create_scraper()
        soup = BeautifulSoup(scraper.get(url).text)
        return soup

    # Obtenemos una lista de listas con el año y su enlance correspondiente dentro de la página
    # [[año, "link"]]
    def __getYearsLinks__(self, html):
        lstYearsLinks = []

        for link in html.find_all('a'):
            lstYearsLinks.append([int(link.text), link['href']])

        return lstYearsLinks

    # Método main para realizar el web-scraping
    def __scraping__(self):
        lstYearsLinks = []
        self.soup = self.__getHtml__(self.url)
        
        # Obtenemos los años juntos con sus enlaces
        eTable = self.soup.find('table') #Obtenemos la primera tabla en la cual se encuentran los años por temporada
        lstYearsLinks = self.__getYearsLinks__(eTable)
        print(lstYearsLinks)