from repositories import repository
from models import oferta_detalle

class OfertaDetalleDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def insert_then_return_latest_row(self, oferta_detalle: oferta_detalle.OfertaDetalle):
        # defino las sentencia sql
        sql_insert = "INSERT INTO public.oferta_detalle(id_oferta, descripcion, descripcion_normalizada, ind_activo," \
                     " motivo_inactivo, fecha_creacion, fecha_modificacion, ofertaperfil_id) " \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        sql_select_last = "SELECT last_value FROM oferta_detalle_id_ofertadetalle_seq"

        params = (
            oferta_detalle.getIdOferta(),
            oferta_detalle.getDescripcion(),
            oferta_detalle.getDescripcionNormalizada(),
            oferta_detalle.getIndActivo(),
            oferta_detalle.getMotivoInactivo(),
            oferta_detalle.getFechaCreacion(),
            oferta_detalle.getFechaModificacion(),
            oferta_detalle.getOfertaPerfilId()
            )

        return self.__repository.insert_then_return_latest_row(params, sql_insert, sql_select_last)