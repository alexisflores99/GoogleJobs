import random
from time import sleep
from datetime import datetime
from utils import util
# Para expresiones regulares
import re
import hashlib
from unicodedata import normalize

# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
## Verifica si hay una version actual de chromedriver y sino lo descarga automaticamente
import chromedriver_autoinstaller
# Modelos
from models import oferta as ofertaModelo
from models import oferta_detalle
from models import webscraping
# Servicios
from services import oferta_service
from services import oferta_detalle_service
from services import keyword_search_service
# Dao
from dao import webscraping_dao

# Traemos a los properties
from properties.configuration import *


# Inicio del driver
# driver = webdriver.Chrome('./chromedriver.exe')
# Sirve para ir a la pagina que le queremos hacer scraping 
# driver.get('https://www.google.com/search?sxsrf=ALeKk03XK7NcEYLQRWLPJL4BR6Ant4F4uw:1607891015641&source=hp&ei=R3jWX4LYJIf45gKpoaqoBw&q=ANALISTA+SISTEMAS&oq=convocatoria+analista+programador&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzoCCAA6CAgAELEDEIMBOgUIABCxAzoICC4QsQMQgwE6BAgAEAo6BQgAEMsBOgcIIxCxAhAnOgcIABCxAxAKOgoIABCxAxCDARAKOgYIABAWEB46BQghEKABUJQcWNydAWChqAFoBHAAeAGAAa0CiAGNPZIBCTAuMTQuMjIuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&uact=5&ibp=htl;jobs&sa=X&ved=2ahUKEwiZt6nz5MvtAhVHwFkKHXCqBVIQudcGKAJ6BAgDEBY&sxsrf=ALeKk018W8_O9N53kUNgBwJEq6JcmPc1hw:1607891042335#fpstate=tldetail&htivrt=jobs&htidocid=s3Vwog73NG3iEqHzAAAAAA%3D%3D') 


# Aqui seleccionamos al scroll
# scroll_empleos = driver.find_element_by_class_name("vWdgBe") 

class WebScrapingService():
    def __init__(self):
        # del paquete dao/webscraping_dao inyecta la clase WebscrapingDao
        self.__wscraping_dao = webscraping_dao.WebscrapingDao()
        # del paquete service/oferta inyecta la clase OfertaService
        self.__of_service = oferta_service.OfertaService()
        # del paquete service/oferta_detalle_service inyecta la clase OfertaDetalleService
        self.__of_detalle_service = oferta_detalle_service.OfertaDetalleService()
        # del paquete service/keyword_search_service inyecta la clase KeywordSearchService
        self.__key_service = keyword_search_service.KeywordSearchService()

    # 5) Recuperamos la posicion insertada en la tabla 'webscraping'
    def insert_then_return_latest_row(self, webscraping: webscraping.WebScraping):
        # Devuelve la posicion del row de la tabla
        return self.__wscraping_dao.insert_then_return_latest_row(webscraping)

    # 3) Iteramos y traemos todos los keyword_search() de nuestra db
    def iterar_scrape(self):
        ksearchs = self.__key_service.select_keyword_search()
        for ksearch in ksearchs:
            cadena_limpia = util.Utils().limpiar_cadena(ksearch[1])

            # Llamamos al scrape_request
            self.scrape_request(cadena_limpia, ksearch[0])

    # 4) Este metodo recibe (el key_word palabra,el id del key_word)
    def scrape_request(self, cadena_busqueda, id_keyword):
        pagina_web = GOOGLE_JOBS["WS_PORTAL_LABORAL"]               ## google jobs
        numero_paginas = GOOGLE_JOBS["WS_PAGINAS"]                  ## 1
        url_pagina = GOOGLE_JOBS["WS_PORTAL_LABORAL_URL"]           ## https://google.com

        ## incrusto mi keyword search en la url
        url_busqueda = "/search?q="+cadena_busqueda+"&ibp=htl;jobs#htivrt=jobs"
        url_busqueda = url_pagina + url_busqueda

        print(url_busqueda)
        print(numero_paginas)
        print('==========')

        ## creamos una instancia de webscraping
        wscraping = webscraping.WebScraping(
            None,                       # busqueda
            None,                       # busqueda_area
            pagina_web,                 # pagina_web
            url_pagina,                 # url_pagina
            url_busqueda,               # url_busqueda
            id_keyword                  # id_keyword
        )
        id_webscraping_insert = self.insert_then_return_latest_row(wscraping)
        self.scrape(url_busqueda, numero_paginas, id_webscraping_insert)


    # 1) Scrapeando la pagina (url de la pagina,numero de paginas que queremos,id del scraping)
    def scrape(self, url_pagina, numero_paginas, id_webscraping):

        # Instalador
        chromedriver_autoinstaller.install()
        # inicio el driver
        ## Se abriran varias paginas con los key_works buscados en googleJobs
        driver = webdriver.Chrome()
        # url de la pagina que queremos scrapear
        driver.get(url_pagina)
       # Aqui seleccionamos al scroll
        scroll_empleos = driver.find_element_by_class_name("vWdgBe") 

        for x in range(0,numero_paginas):
            # Bajamos el scroll 
            scroll_empleos.send_keys(Keys.END)
            sleep(random.uniform(0.5, 1))

        scroll_empleos.send_keys(Keys.UP)

        # obtengo todos los titulos de los trabajos
        # Se le da click al titulo para que muestre el detalle
        titulos = driver.find_elements_by_class_name("BjJfJf")  

        for titulo in titulos:

            item_detalle = driver.find_element_by_class_name("jolnDe")  # item contenedor
            titulo.click()
            sleep(random.uniform(0.5, 1))
            # empresa y lugar
            etiquetas = item_detalle.find_elements_by_class_name("sMzDkb")
            # detalle del trabajo
            detalle = item_detalle.find_element_by_class_name("HBvzbc")
        
            # url 
            url_oferta = item_detalle.find_element_by_class_name("pMhGee").get_attribute('href')
            # tiempo publicado
            tiempo_publicado = item_detalle.find_element_by_class_name("SuWscb").text

            empresa = ""
            lugar = ""

            try:
                empresa = etiquetas[0].text
                lugar = etiquetas[1].text
            except:
                pass

            # Si tiene un boton de mas detalle le damos click y vemos mas detalle de ese trabajo
            try:
                masInfo = item_detalle.find_element_by_class_name("cVLgvc")
                masInfo.click()
            except:
                pass

            # Cifra para sacar el id anuncio 
            id_anuncioempleo = hashlib.md5(str(detalle.text).encode()).hexdigest()

            # Creamos la oferta Modelo
            ofer = ofertaModelo.Oferta(
                        id_webscraping,                 # id_webscraping
                        titulo.text,                    # titulo
                        empresa,                        # empresa
                        lugar,                          # lugar
                        tiempo_publicado,               # tiempo publicado
                        None,                           # salario
                        None,                           # modalidad de trabajo
                        None,                           # subarea
                        url_oferta,                     # url oferta
                        url_pagina,                     # url pagina
                        None,                           # area
                        datetime.now(),                 # fecha creacion
                        datetime.now(),                 # fecha modificacion
                        detalle.text,                   # detalle
                        None,                           # fecha publicacion
                        id_anuncioempleo                # id_anuncioempleo
                    )
            
            # print(ofer)

            # recibe como paramaetro 'insert_then_return_latest_row(ofertaModelo.Oferta)'
            # devuelve el ultimo id_oferta que se inserto
            # esto me va servir para insertar en oferta detalle
            # Esto me devuel la pos de la consulta 
            # Ejemplo 1,2,3 ....... 40 -> si fuera la iteracion 22 me devuelve (22 + row.oferta)
            id_oferta_insert = self.__of_service.insert_then_return_latest_row(ofer)
            parrafo = detalle.text.splitlines()
            # Limpiamos el parrafo
            self.limpiarParrafo(parrafo, id_oferta_insert)

    # 2) Limpiamos el parrafo
    def limpiarParrafo(self, parrafo, id_oferta):
        for linea_descripcion in parrafo:
            linea_descripcion = linea_descripcion.strip()
            if (len(linea_descripcion) > 0):
                if (not linea_descripcion[0].isalpha()):
                    linea_descripcion = linea_descripcion[1:]
                linea_descripcion = linea_descripcion.strip().upper()
                linea_descripcion = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                              normalize("NFD", linea_descripcion), 0, re.I)
                if (not linea_descripcion == ""):
                    # inserto cada linea en oferta_detalle
                    self.__of_detalle_service.insert_then_return_latest_row(
                    oferta_detalle.OfertaDetalle(
                        id_oferta,                          # id_oferta
                        linea_descripcion,                  # descripcion
                        None,                               # descripcion normalizada
                        None,                               # ind_activo            (entero)
                        None,                               # modo_inactivo         (entero)
                        datetime.now(),                     # fecha_creacion        (fecha)
                        datetime.now(),                     # fecha_modificacion    (fecha)
                        None                                # ofertaperfil_id       (entero)
                    ))

web = WebScrapingService()
# web.scrape(1,1,1)
web.iterar_scrape()