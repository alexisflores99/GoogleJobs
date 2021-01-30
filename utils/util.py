import datetime
import re

class Utils():

    meses = [
        ['enero', 31],
        ['febrero', 28],
        ['marzo', 30],
        ['abril', 31],
        ['mayo', 30],
        ['junio', 31],
        ['julio', 31],
        ['agosto', 31],
        ['septiembre', 30],
        ['octubre', 31],
        ['noviembre', 30],
        ['diciembre', 31]
    ]

    def limpiar_cadena(self, cadena):
        return cadena.replace(" ","+")

    def obtenerModalidad(self, parrafo, titulo):
        for linea_descripcion in parrafo:
            linea_descripcion = linea_descripcion.strip()
            if self.isModalidad(linea_descripcion, titulo) == "REMOTO":
                return "Remoto"
            if self.isModalidad(linea_descripcion, titulo) == "PRESENCIAL":
                return "Presencial"

    def obtenerSalario(self, parrafo):
        for linea_descripcion in parrafo:
            linea_descripcion = linea_descripcion.strip()
            if self.isSalario(linea_descripcion):
                return linea_descripcion

    def isModalidad(self, lineaTexto, titulo):
        modalidad_remoto = ["REMOTO", "REMOTA", "TELETRABAJO"]
        modalidad_presencial = ["PRESENCIAL"]
        for modalidad in modalidad_remoto:
            if (modalidad.lower() in lineaTexto.lower()) or (modalidad.lower() in titulo.lower()):
                return "REMOTO"

        for modalidad in modalidad_presencial:
            if (modalidad.lower() in lineaTexto.lower()):
                return "PRESENCIAL"

    def isSalario(self, lineaTexto):
        salario_keywords = ["SUELDO", "SALARIO", "REMUNERACION", "REMUNERACIÓN", "ESTIPENDIO"
                            "RETRIBUCION", "RETRIBUCIÓN", "HONORARIO", "GRATIFICACION",
                            "GRATIFICACIÓN", "SUBVENCION", "SUBVENCIÓN", "PENSION", "PENSIÓN"]
        for salario in salario_keywords:
            if (salario.lower() in lineaTexto.lower()):
                return True

    def obtener_numero_fecha(self, cadena):
        print("cadena: " +cadena)
        return int(re.sub("[^0-9]", "", cadena))    #########

    def obtener_fec_pub(self, cadena):
        # Hace una referencia a fecha actual
        fecha_actual = datetime.datetime.now()
        hora_actual = fecha_actual.hour
        dia_actual = fecha_actual.day
        mes_actual = fecha_actual.month
        anio_actual = fecha_actual.year

        if ("hora" in cadena) or ("día" in cadena) or ("mes" in cadena):

            numero = self.obtener_numero_fecha(cadena)  ######

            if "hora" in cadena:
                if hora_actual >= numero:
                    return datetime.date(anio_actual, mes_actual, dia_actual)
                else:
                    if dia_actual != 1:
                        return datetime.date(anio_actual, mes_actual, dia_actual - 1)
                    else:
                        if mes_actual != 1:
                            return datetime.date(anio_actual, mes_actual - 1, meses[mes_actual - 1][1])
                        else:
                            return datetime.date(anio_actual - 1, 12, 31)

            if "día" in cadena:
                if dia_actual > numero:
                    return datetime.date(anio_actual, mes_actual, dia_actual - numero)
                else:
                    if mes_actual == 1:
                        return datetime.date(anio_actual - 1, 12, 31 - abs(dia_actual - numero))
                    else:
                        return datetime.date(anio_actual, mes_actual - 1, meses[mes_actual - 1][1] - abs(dia_actual - numero))

            if "mes" in cadena:
                if mes_actual > numero:
                    return datetime.date(anio_actual, mes_actual - numero, dia_actual)
                else:
                    return datetime.date(anio_actual - 1, 12 - abs(mes_actual - numero), dia_actual)

        else:
            return None

    