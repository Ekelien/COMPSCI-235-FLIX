from difflib import SequenceMatcher
import random
from flix.adapters.repository import AbstractRepository
from flix.data.csv_reader import MovieFileCSVReader


class FlixRepository(AbstractRepository):
    def __init__(self, filepath="flix/data/Data1000Movies.csv"):
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

    def random_movie(self, genre=None,number=12):
        return_list=[]
        i=0
        if not genre:
            return
        while i<number:
            random_num=random.randrange(0,len(genre))
            movie_list=self.data.dataset_of_genre[genre[random_num]]
            movie=random.choice(movie_list)
            if movie not in return_list:
                return_list.append(movie)
                i+=1
        return return_list