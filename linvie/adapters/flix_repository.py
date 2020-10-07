import string
from difflib import SequenceMatcher
import random
from linvie.adapters.repository import AbstractFlixRepository
from linvie.adapters.csv_reader import MovieFileCSVReader


class FlixRepository(AbstractFlixRepository):
    def __init__(self, filepath="linvie/data/Data1000Movies.csv"):
        self.data = MovieFileCSVReader(filepath)
        self.data.read_csv_file()

    def find(self, keyword: str):
        keyword = keyword.strip()
        match = []
        similar = []
        for lis in [self.data.dataset_of_movie, self.data.dataset_of_people]:
            for item in lis:
                similarity = SequenceMatcher(None, item.name.lower(), keyword.lower()).ratio()
                if similarity == 1:  # found
                    match.append(item)
                elif similarity >= 0.7:
                    similar.append(item)
                elif keyword.lower() in item.name.lower():
                    similar.append(item)
        return match, similar

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

    def random_movie(self, genre=None, number=12):
        return_list = []
        i = 0
        if not genre:
            return
        while i < number:
            random_num = random.randrange(0, len(genre))
            movie_list = self.data.dataset_of_genre[genre[random_num]]
            movie = random.choice(movie_list)
            if movie not in return_list:
                return_list.append(movie)
                i += 1
        return return_list

    def find_movie(self, keyword):
        for movie in self.data.dataset_of_movie:
            if movie.name == keyword:
                return movie

    def find_people(self, keyword):
        for person in self.data.dataset_of_people:
            if person.name == keyword:
                return person

    def sorted_dictionary(self, keyword):
        return_dict = {}
        for letter in string.ascii_uppercase:
            return_dict[letter] = []
        return_dict["#"] = []
        if keyword=="actor":
            iter_list = self.data.dataset_of_actors
        elif keyword=="director":
            iter_list = self.data.dataset_of_director
        elif keyword=="genre":
            iter_list = self.data.dataset_of_genre.keys()
        else:
            raise TypeError
        for item in iter_list:
            try:
                return_dict[item.name[0].upper()].append(item)
            except:
                return_dict["#"].append(item)
        return return_dict

    @staticmethod
    def search_index():
        alphabet = list(string.ascii_uppercase)
        alphabet.append("#")
        return alphabet

