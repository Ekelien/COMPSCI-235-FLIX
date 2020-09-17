from abc import ABC,abstractmethod
from difflib import SequenceMatcher
from flix.data.csv_reader import MovieFileCSVReader
from flix.domainmodel.actor import Actor
from flix.domainmodel.director import Director
from flix.domainmodel.genre import Genre
from flix.domainmodel.movie import Movie

database=None

class AbstractRepository(ABC):
    @abstractmethod
    def find(self,keyword):
        raise NotImplementedError

    @abstractmethod
    def movie_filter(self,director,actor:list,genre:list,start_year,end_year):
        raise NotImplementedError

    @abstractmethod
    def random_movie(self,genre=None):
        raise NotImplementedError


class FlixRepository(AbstractRepository):
    def __init__(self):
        self.data=MovieFileCSVReader("Data1000Movies.csv")
        self.data.read_csv_file()

    def find(self,keyword:str):
        keyword=keyword.strip()
        match=[]
        similar=[]
        for lis in [self.data.dataset_of_movie, self.data.dataset_of_director, self.data.dataset_of_actors]:
            for item in lis:
                similarity = SequenceMatcher(None, item.name.lower(), keyword.lower())
                if similarity == 1:  # found
                    match.append(item)
                elif similarity >= 0.7:
                    similar.append(item)
                elif keyword.lower() in item.actor_full_name.lower():
                    similar.append(item)
        if match!=[]:
            return match
        return similar

    def movie_filter(self,director,actor:list,genre:list,start_year,end_year):
        pass

    def random_movie(self,genre=None):
        pass


