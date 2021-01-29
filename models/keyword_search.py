class keywordSearch():

    def __init__(self, id_keyword, descripcion):
        self._id_keyword = id_keyword
        self.__descripcion=descripcion



    ## setters

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setIdkeyword(self, id_keyword):
        self.__id_keyword = id_keyword

    ## getters

    def getDescripcion(self):
        return self.__descripcion

    def getIdkeyword(self):
        return self.__id_keyword

