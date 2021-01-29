from dao import oferta_detalle_dao
from models import oferta_detalle

class OfertaDetalleService():

    def __init__(self):
        self.__oferta_detalle_dao = oferta_detalle_dao.OfertaDetalleDao()

    def insert_then_return_latest_row(self, oferta_detalle: oferta_detalle.OfertaDetalle):
        return self.__oferta_detalle_dao.insert_then_return_latest_row(oferta_detalle)