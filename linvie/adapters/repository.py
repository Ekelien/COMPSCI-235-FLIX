import string
from abc import ABC, abstractmethod

database = None
users=None


class AbstractFlixRepository(ABC):
    @abstractmethod
    def find(self, keyword):
        raise NotImplementedError

    @abstractmethod
    def movie_filter(self, director=None, actor: list = None, genre: list = None, start_year: int = None,
                     end_year: int = None):
        raise NotImplementedError

    @abstractmethod
    def random_movie(self, genre=None):
        raise NotImplementedError

    @abstractmethod
    def find_movie(self,keyword):
        raise NotImplementedError

    @abstractmethod
    def find_people(self,keyword):
        raise NotImplementedError



class AbstractUserRepository(ABC):

    @abstractmethod
    def get_user(self,username):
        raise NotImplementedError

