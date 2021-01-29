class Oferta():

    def __init__(self, id_webscraping, titulo, empresa, lugar,
     tiempo_publicado, salario, modalidad_trabajo, subarea,
     url_oferta, url_pagina, area, fecha_creacion, fecha_modificacion
     ,oferta_detalle, oferta_fecha_publicacion, id_anuncioempleo):
        self.__id_webscraping=id_webscraping
        self.__titulo=titulo
        self.__empresa=empresa
        self.__lugar=lugar
        self.__tiempo_publicado=tiempo_publicado
        self.__salario=salario
        self.__modalidad_trabajo=modalidad_trabajo
        self.__subarea=subarea
        self.__url_oferta=url_oferta
        self.__url_pagina=url_pagina
        self.__area=area
        self.__fecha_creacion=fecha_creacion
        self.__fecha_modificacion=fecha_modificacion
        self.__oferta_detalle=oferta_detalle
        self.__oferta_fecha_publicacion = oferta_fecha_publicacion
        self.__id_anuncioempleo = id_anuncioempleo

    ## setters
    def setId_webscraping(self, id_webscraping):
        self.__id_webscraping = id_webscraping

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setEmpresa(self, empresa):
        self.__empresa = empresa

    def setLugar(self, lugar):
        self.__lugar = lugar

    def setTiempo_publicado(self, tiempo_publicado):
        self.__tiempo_publicado = tiempo_publicado

    def setSalario(self, salario):
        self.__salario = salario

    def setModalidad_trabajo(self, modalidad_trabajo):
        self.__modalidad_trabajo = modalidad_trabajo

    def setSubarea(self, subarea):
        self.__subarea = subarea

    def setUrl_oferta(self, url_oferta):
        self.__url_oferta = url_oferta

    def setUrl_pagina(self, url_pagina):
        self.__url_pagina = url_pagina

    def setArea(self, area):
        self.__area = area

    def setFecha_creacion(self, fecha_creacion):
        self.__fecha_creacion = fecha_creacion

    def setFecha_modificacion(self, fecha_modificacion):
        self.__fecha_modificacion = fecha_modificacion

    def setOferta_detalle(self, oferta_detalle):
        self.__oferta_detalle = oferta_detalle

    def setOfertaFechaPublicacion(self, oferta_fecha_publicacion):
        self.__oferta_fecha_publicacion = oferta_fecha_publicacion

    def setIdAnuncioEmpleo(self, id_anuncioempleo):
        self.__id_anuncioempleo = id_anuncioempleo

    ## getters
    def getId_webscraping(self):
        return self.__id_webscraping

    def getTitulo(self):
        return self.__titulo

    def getEmpresa(self):
        return self.__empresa

    def getLugar(self):
        return self.__lugar

    def getTiempo_publicado(self):
        return self.__tiempo_publicado

    def getSalario(self):
        return self.__salario

    def getModalidad_trabajo(self):
        return self.__modalidad_trabajo

    def getSubarea(self):
        return self.__subarea

    def getUrl_oferta(self):
        return self.__url_oferta

    def getUrl_pagina(self):
        return self.__url_pagina

    def getArea(self):
        return self.__area

    def getFecha_creacion(self):
        return self.__fecha_creacion

    def getFecha_modificacion(self):
        return self.__fecha_modificacion

    def getOferta_detalle(self):
        return self.__oferta_detalle

    def getOfertaFechaPublicacion(self):
        return self.__oferta_fecha_publicacion

    def getIdAnuncioEmpleo(self):
        return self.__id_anuncioempleo

    # toString
    def __repr__(self):
        return str(self.__dict__)