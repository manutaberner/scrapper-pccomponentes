Práctica 1: Web scraping
Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web PlaneCrashInfo y generar un dataset.

Miembros del equipo
La actividad ha sido realizada de manera individual por Teguayco Gutiérrez González.

Ficheros del código fuente
src/main.py: punto de entrada al programa. Inicia el proceso de scraping.
src/scraper.py: contiene la implementación de la clase AccidentsScraper cuyos métodos generan el conjunto de datos a partir de la base de datos online PlaneCrashInfo.
src/reason_classifier.py: contiene la implementación de la clase que se encarga de asignar una causa a un resumen de accidente dado. Para ello, utiliza la librería TextBlob.
Recursos
Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
