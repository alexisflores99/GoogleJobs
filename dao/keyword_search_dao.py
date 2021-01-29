from repositories import repository
from models import keyword_search

class KeywordSearchDao():

    def __init__(self):
        self.__repository = repository.Repository()

    def select_keyword_search(self):
        # defino las sentencia sql
        sql_select = "SELECT id_keyword, descripcion FROM public.keyword_search"

        return self.__repository.select_keyword_search(sql_select)