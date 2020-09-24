from abc import ABC, abstractmethod
from difflib import SequenceMatcher
from flix.data.csv_reader import MovieFileCSVReader
from flix.domainmodel.actor import Actor
from flix.domainmodel.director import Director
from flix.domainmodel.genre import Genre
from flix.domainmodel.movie import Movie

database = None


class AbstractRepository(ABC):
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



