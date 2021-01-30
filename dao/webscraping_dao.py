from repositories import repository
from models import webscraping

class WebscrapingDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def insert_then_return_latest_row(self, webscraping):
        # defino las sentencia sql
        sql_insert = "INSERT INTO webscraping (busqueda, busqueda_area, pagina_web, url_pagina, url_busqueda,fecha_creacion,fecha_modificacion, id_keyword, delati_team)" \
                     "VALUES (%s, %s, %s, %s, %s, current_date, current_date, %s,'Devcito')"

        sql_select_last = "SELECT last_value FROM webscraping_id_webscraping_seq"

        # obtengo los parametros para la query sql
        params = (
            webscraping.getBusqueda(),
            webscraping.getBusquedaArea(),
            webscraping.getPagina_web(),
            webscraping.getUrl_pagina(),
            webscraping.getUrl_busqueda(),
            webscraping.getId_keyword())

        return self.__repository.insert_then_return_latest_row(params, sql_insert, sql_select_last)
