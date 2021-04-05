# IMPORTS
import cloudscraper
from bs4 import BeautifulSoup
import datetime
import re
import calendar

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
        soup = BeautifulSoup(scraper.get(url).text, 'html.parser')
        return soup

    # Obtenemos una lista de listas con el año y su enlance correspondiente dentro de la página
    # [[año, "link"]]
    def __getYearsLinks__(self, html):
        lstYearsLinks = []

        for link in html.find_all('a'):
            year = int(link.text)
            if year < datetime.datetime.now().year: # Si ha acabado la temporada
                lstYearsLinks.append([year, link['href']])

        return lstYearsLinks

    # Método que comprueba una fecha, devuevle True si es correcto el año, mes y día. False en caso contrario
    def __checkDate__(self, year, sMonthDay):
        # Comprobamos el año
        if (year < 1950 or year > datetime.datetime.now().year):
            return False
        # Comprobamos el mes y día
        if (len(sMonthDay) == 0):
            return False

        return True

    # Método que devuelve el número del mes a partir de su nombre
    def __getMonth__(self, month):
        monthNumber = {}
        for i in range(1,13):
            monthNumber[calendar.month_name[i]]=i
        return monthNumber[month]

    # Método que converite una fecha de tipo Month [space] Day, al tipo Day/Month/Year
    def __getDate__(self, year, sMonthDay):
        date = datetime.date.today().strftime("%d/%m/%Y")

        if (self.__checkDate__(year, sMonthDay)):
            lstMonthDay = re.split(r"\s+", sMonthDay)
            month = lstMonthDay[0]
            day = lstMonthDay[1]
            date = day.zfill(2) + "/" + str(self.__getMonth__(month)).zfill(2) + "/" + str(year)
            
        return date

    # Método que obtiene los minutos por vuelta
    def __getTimeLap__(self, laps, time):
        laps = int(laps)
        lstTime = time.split(":")
        hours = int(lstTime[0])
        minutes = int(lstTime[1])
        seconds = int(lstTime[2].split(".")[0])
        miliseconds = int(lstTime[2].split(".")[1])

        # Conversión a minutos
        hours = hours * 60
        seconds = seconds / 60
        miliseconds = (miliseconds / 1000) / 60
        minutes = minutes + hours + seconds + miliseconds

        minLap = minutes / laps
        minutes = int(minLap)
        seconds = int(abs(minLap - minutes) * 60)
        miliseconds = int(round(abs(seconds - (abs(minLap - minutes) * 60)), 3) * 1000)
        
        return str(minutes) + ":" + str(seconds) + "." + str(miliseconds) 

    # Método que va almacenando la data según el año
    def __getData__(self, year, link):
        self.soup = self.__getHtml__(link)
        eTable = self.soup.find('table')
    
        for eTr in eTable.select('tbody > tr'): # Nos quedamos con las filas de la tabla que contienen datos
            lstRow = []

            for eTd, i in zip(eTr.find_all('td'), range(0, len(eTr.contents))): # Recorremos las columnas de la tabla
                if (eTd is not None):
                    # Columna Race
                    if (i == 0):
                        lstRow.append(eTd.text)
                    # Columna Date
                    if (i == 1):
                        sDate = eTd.text #String de la fecha con el formato Month [space] day
                        lstRow.append(self.__getDate__(year, sDate))
                    # Columna Winner y Team
                    if (i == 2 or i == 3):
                        nationality = eTd.find('img')['alt']
                        winner = eTd.find_all('a')[1]['title']
                        lstRow.append(nationality)
                        lstRow.append(winner)
                    # Columna Laps
                    if (i == 4):
                        laps = int(str(eTd.text))
                        lstRow.append(laps)
                    # Columna Time
                    if (i == 5):
                        lstRow.append(eTd.text)
                        # Creamos una nueva columna para los tiempos por vuelta
                        lstRow.append(self.__getTimeLap__(laps, eTd.text))
                else:
                    lstRow.append("Na")
    
            self.data.append(lstRow)

    # Método main para realizar el web-scraping
    def __scraping__(self):
        lstYearsLinks = []
        self.soup = self.__getHtml__(self.url)
        
        # Obtenemos los años juntos con sus enlaces
        eTable = self.soup.find('table') #Obtenemos la primera tabla en la cual se encuentran los años por temporada
        lstYearsLinks = self.__getYearsLinks__(eTable)

        for yearLink in lstYearsLinks:
            year = yearLink[0]
            link = yearLink[1]
            self.__getData__(year, link)

        return self.data