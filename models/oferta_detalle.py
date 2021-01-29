class OfertaDetalle():

    def __init__(self, id_oferta, descripcion, descripcion_normalizada, ind_activo,
     motivo_inactivo, fecha_creacion, fecha_modificacion, ofertaperfil_id):
        self.__id_oferta = id_oferta
        self.__descripcion = descripcion
        self.__descripcion_normalizada = descripcion_normalizada
        self.__ind_activo = ind_activo
        self.__motivo_inactivo = motivo_inactivo
        self.__fecha_creacion = fecha_creacion
        self.__fecha_modificacion = fecha_modificacion
        self.__ofertaperfil_id = ofertaperfil_id

    def getIdOferta(self):
        return self.__id_oferta

    def getDescripcion(self):
        return self.__descripcion

    def getDescripcionNormalizada(self):
        return self.__descripcion_normalizada

    def getIndActivo(self):
        return self.__ind_activo

    def getMotivoInactivo(self):
        return self.__motivo_inactivo

    def getFechaCreacion(self):
        return self.__fecha_creacion

    def getFechaModificacion(self):
        return self.__fecha_modificacion

    def getOfertaPerfilId(self):
        return self.__ofertaperfil_id

    def setIdOferta(self, id_oferta):
        self.__id_oferta = id_oferta