from repositories.dbconnection import Connection
import psycopg2

class Repository():

    def __init__(self):
        self.__conexion = Connection()

    # Este metodo sirve para insertar en la base de datos
    # Ya sea en cualquier tipo de base de datos
    # Solo necesita los parametros 
    # Sql a insertar
    # Y el slq del ultimo insertado
    def insert_then_return_latest_row(self, params, sql_insert, sql_select_last):
        last_row_id = 0
        try:

            # conecto a base de datos
            database = self.__conexion.connect()

            # ejecuto la query
            cursor = database.cursor()
            cursor.execute(sql_insert, params)

            # confirmo cambios
            database.commit()
            print("Sentencia ejecutada")

            # obtengo el id del ultimo registro insertado
            cursor.execute(sql_select_last)
            last_row_id = int(cursor.fetchone()[0])

        except (Exception, psycopg2.DatabaseError) as error:
            # revertir en caso de error
            print("Error!, rollback")
            print(error)
            database.rollback()

        database.close()
        return last_row_id

    # Devuelve las palabras claves
    def select_keyword_search(self, sql_select):
        keywords = []
        try:

            # conecto a base de datos
            database = self.__conexion.connect()

            # ejecuto la query
            cursor = database.cursor()

            # obtengo keywords
            cursor.execute(sql_select)
            keywords = list(cursor.fetchall())

        except (Exception, psycopg2.DatabaseError) as error:
            # revertir en caso de error
            print("Error!, rollback")
            print(error)

        database.close()
        return keywords

    def insert(self, params, sql_insert):
        last_row_id = 0
        try:

            # conecto a base de datos
            database = self.__conexion.connect()

            # ejecuto la query
            cursor = database.cursor()
            cursor.execute(sql_insert, params)

            # confirmo cambios
            database.commit()
            print("Sentencia ejecutada")

        except (Exception, psycopg2.DatabaseError) as error:
            # revertir en caso de error
            print("Error!, rollback")
            print(error)
            database.rollback()

        database.close()

    