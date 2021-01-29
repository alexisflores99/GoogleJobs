class WebScraping():

    def __init__(self, busqueda, busqueda_area, pagina_web,
     url_pagina, url_busqueda, id_keyword):
        self.__busqueda = busqueda
        self.__busqueda_area = busqueda_area
        self.__pagina_web = pagina_web
        self.__url_pagina = url_pagina
        self.__url_busqueda = url_busqueda
        self.__id_keyword = id_keyword

    ## setters
    def setId_webscraping(self, id_webscraping):
        self.__id_webscraping = id_webscraping

    def setBusqueda(self, busqueda):
        self.__busqueda = busqueda

    def setBusquedaArea(self, busqueda_area):
        self.__busqueda_area = busqueda_area

    def setPagina_web(self, pagina_web):
        self.__pagina_web=pagina_web

    def setUrl_pagina(self, url_pagina):
        self.__url_pagina=url_pagina

    def setUrl_busqueda(self, url_busqueda):
        self.__url_busqueda=url_busqueda

    def setId_keyword(self, id_keyword):
        self.__id_keyword=id_keyword

    ## getters
    def getId_webscraping(self):
        return self.__id_webscraping

    def getBusqueda(self):
        return self.__busqueda

    def getBusquedaArea(self):
        return self.__busqueda_area

    def getPagina_web(self):
        return self.__pagina_web

    def getUrl_pagina(self):
        return self.__url_pagina

    def getUrl_busqueda(self):
        return self.__url_busqueda

    def getId_keyword(self):
        return self.__id_keyword

    def toString(self):
        print(f"Pagina web: #{self.__pagina_web}" f"\tUrl pagina: {self.__url_pagina}" f"\tKeyword: {self.__id_keyword}")