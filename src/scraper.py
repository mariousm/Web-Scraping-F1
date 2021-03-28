# IMPORTS
import cloudscraper
from bs4 import BeautifulSoup
import datetime
import re

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

    # Método que comprueba una fecha, devuevle True si es correcto el año, mes y día. False en caso contrario
    def __checkDate__(self, year, sMonthDay):
        # Comprobamos el año
        if (year < 1950 or year >= datetime.datetime.now().year):
            return False
        # Comprobamos el mes y día
        if (len(sMonthDay) == 0):
            return False

        return True

    # Método que devuelve el número del mes a partir de su nombre
    def __getMonth__(self, month):
        if (month == "January"):
            return "01"
        if (month == "February"):
            return "02"
        if (month == "March"):
            return "03"
        if (month == "April"):
            return "04"
        if (month == "May"):
            return "05"
        if (month == "June"):
            return "06"
        if (month == "July"):
            return "07"
        if (month == "August"):
            return "08"
        if (month == "September"):
            return "09"
        if (month == "October"):
            return "10"
        if (month == "November"):
            return "11"
        if (month == "December"):
            return "12"

    # Método que converite una fecha de tipo Month [space] Day, al tipo Day/Month/Year
    def __getDate__(self, year, sMonthDay):
        date = datetime.date.today().strftime("%d/%m/%Y")

        if (self.__checkDate__(year, sMonthDay)):
            lstMonthDay = re.split(r"\s+", sMonthDay)
            month = lstMonthDay[0]
            day = lstMonthDay[1]
            date = day.zfill(2) + "/" + self.__getMonth__(month) + "/" + str(year)
            

        return date

    # Método main para realizar el web-scraping
    def __scraping__(self):
        lstYearsLinks = []
        self.soup = self.__getHtml__(self.url)
        
        # Obtenemos los años juntos con sus enlaces
        eTable = self.soup.find('table') #Obtenemos la primera tabla en la cual se encuentran los años por temporada
        lstYearsLinks = self.__getYearsLinks__(eTable)
        
        # -------------------
        year = lstYearsLinks[0][0]
        link = lstYearsLinks[0][1]

        self.soup = self.__getHtml__(link)
        eTable = self.soup.find('table')
        
        for eTr in eTable.select('tbody > tr'): # Nos quedamos con las filas de la tabla que contienen datos
            lstRow = []

            for eTd, i in zip(eTr.find_all('td'), range(0, len(eTr.contents))): # Recorremos las columnas de la tabla
                # Si i == 0 -> Columna Race
                if (i == 0):
                    lstRow.append(eTd.text)
                # Si i == 1 -> Columna Date
                if (i == 1):
                    sDate = eTd.text #String de la fecha con el formato Month [space] day
                    lstRow.append(self.__getDate__(year, sDate))

            print(lstRow)