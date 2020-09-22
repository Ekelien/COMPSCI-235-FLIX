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


class FlixRepository(AbstractRepository):
    def __init__(self, filepath):
        self.data = MovieFileCSVReader(filepath)
        self.data.read_csv_file()

    def find(self, keyword: str):
        keyword = keyword.strip()
        match = []
        similar = []
        for lis in [self.data.dataset_of_movie, self.data.dataset_of_director, self.data.dataset_of_actors]:
            for item in lis:
                similarity = SequenceMatcher(None, item.name.lower(), keyword.lower()).ratio()
                if similarity == 1:  # found
                    match.append(item)
                elif similarity >= 0.7:
                    similar.append(item)
                elif keyword.lower() in item.name.lower():
                    similar.append(item)
        if match != []:
            return match
        return similar

    def movie_filter(self, genre: list = None, start_year: int = None, end_year: int = None):
        return_list = []
        for movie in self.data.dataset_of_movie:
            indicator = 0
            if genre:
                if all([g in movie.genres for g in genre]):
                    indicator += 1
            else:
                indicator += 1
            if start_year:
                if start_year <= int(movie.time):
                    indicator += 1
            else:
                indicator += 1
            if end_year:
                if int(movie.time) <= end_year:
                    indicator += 1
            else:
                indicator += 1
            if indicator == 3:
                return_list.append(movie)
        return return_list

    def random_movie(self, genre=None):
        pass
