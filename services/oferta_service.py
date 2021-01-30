from dao import oferta_dao
from models import oferta

class OfertaService():

    def __init__(self):
        # del paquete dao/oferta inyecta la clase OfertaDao
        self.__oferta_dao = oferta_dao.OfertaDao()

    def insert_then_return_latest_row(self, oferta: oferta.Oferta):
        # Aca define los parametros,sql a insertar,el ultimo insertado
        return self.__oferta_dao.insert_then_return_latest_row(oferta)


    # Vemos si en caso existe en la base de datos
    def existe_registro(self, id_anuncioempleo):
        return self.__oferta_dao.existe_registro(id_anuncioempleo)