from dao import keyword_search_dao
from models import keyword_search

class KeywordSearchService():

    def __init__(self):
        self.__keyword_search_dao = keyword_search_dao.KeywordSearchDao()

    def select_keyword_search(self):
        return self.__keyword_search_dao.select_keyword_search()