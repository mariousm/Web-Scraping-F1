
import cloudscraper
from bs4 import BeautifulSoup
import os
# Configuramos la url base y la ruta de descarga
url = 'https://www.f1-fansite.com/archive'
ruta = "/Users/moreybagarciacedres/Downloads/ImagenPEC.jpg"
# Se crea el scraper
scraper = cloudscraper.create_scraper()
soup = BeautifulSoup(scraper.get(url).text)
# Se obtiene un array con todas las imágenes de la página
imgList = soup.find_all('img')
# Buscamos entre todas las imágenes obtenidas, la que tenga el texto alternativo que necesitamos
for img in imgList:
    alt=img.get('alt')
    if (alt == "F1 Fansite Race-blog"):
        # Concatenamos la url base (el directorio anterior) con la url obtenida en la propiedad src de la imagen
        url=url+"/.."+img.get('src')
        break
# Comprobamos que hemos obtenido una url
if (url != None):
    # r = requests.get(url, stream = True)
    # Descargamos el contenido de la url obtenida
    data = scraper.get(url)
    if data.status_code == 200:
        # Si el resultado ha sido OK (200) escribimos el fichero en la ruta configurada
        output = open(ruta,"wb")
        output.write(data.content)
        output.close()
        print("Imagen descargada con éxito en " + ruta)
    else:
        print("Error al descargar la imagen")