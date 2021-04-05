# Web-Scraping-F1

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4662943.svg)](https://doi.org/10.5281/zenodo.4662943)

## Descripción

Esta práctica se realiza como parte del Máster en Ciencia de Datos de la Universitat Oberta de Catalunya más concretamente dentro de la asignatura Tipología y ciclo de vida de los datos. El lenguaje de programación elegido para el desarrollo de la misma ha sido Python. En ella se aplican técnicas de web scraping para extraer datos de la web `f1-fansite.com` y generar un dataset con la información resultante.

## Autores

Esta práctica ha sido realizado por **Moreyba García Cedrés** y **Mario Ubierna San Mamés**.

## Ficheros del código fuente


- **src/scraper:** se encarga de hacer el scraping, desde la página inicial, va buscando por la web y obtiene los datos.

- **src/csvmodule:** se define la clase de creación del CSV. A partir de los datos que consigue el scraper, los introduce en un fichero.

- **src/main:** es el programa principal que incia el proceso de scraping y generación del fichero csv con los datos resultantes del scraping. 

- **src/img:** este un proceso independiente a los anteriores se encarga de hacer scraping buscando una imagen concreta y haciendo la descarga de la misma.


## Recursos
1. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
3. Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
4. Chapagain, A. (2019). Hands-On Web Scraping with Python.
