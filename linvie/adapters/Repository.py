import random
import string
from difflib import SequenceMatcher

from linvie.adapters.AbstractRepository import AbstractRepository
from linvie.adapters.CsvIO import CsvIO
from linvie.domainmodel.Genre import Genre


class Repository(AbstractRepository):
    def __init__(self, movie_file_path="linvie/data/movie.csv", user_file_path="linvie/data/user.csv",
                 comment_file_path="linvie/data/comments.csv"):
        self.data = CsvIO(movie_file_path, user_file_path, comment_file_path)
        self.data.read()

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

    def random_movie(self, genre=[], number=12):
        return_list = []
        i = 0
        if genre == []:
            while i < number:
                movie = random.choice(self.data.dataset_of_movie)
                if movie not in return_list:
                    return_list.append(movie)
                    i += 1
            return return_list
        while i < number:
            random_num = random.randrange(0, len(genre))
            movie_list = self.data.dataset_of_genre[genre[random_num]]
            movie = random.choice(movie_list)
            if movie not in return_list:
                return_list.append(movie)
                i += 1
        return return_list

    def first_n_movie(self, number=4):
        return self.data.dataset_of_movie[:number]

    def find_movie(self, movie_id):
        return self.data.dataset_of_movie[int(movie_id)]

    def find_people(self, keyword):
        for person in self.data.dataset_of_people:
            if person.name == keyword:
                return person

    def sorted_dictionary(self, keyword):
        return_dict = {}
        for letter in string.ascii_uppercase:
            return_dict[letter] = []
        return_dict["#"] = []
        if keyword == "actor":
            iter_list = self.data.dataset_of_actors
        elif keyword == "director":
            iter_list = self.data.dataset_of_director
        elif keyword == "genre":
            iter_list = self.data.dataset_of_genre.keys()
        else:
            raise TypeError
        for item in iter_list:
            try:
                return_dict[item.name[0].upper()].append(item)
            except:
                return_dict["#"].append(item)
        return return_dict

    def genre_movie_dictionary(self, genre):
        iter_list = self.data.dataset_of_genre[Genre(genre)]
        return_dict = {}
        for letter in string.ascii_uppercase:
            return_dict[letter] = []
        return_dict["#"] = []
        for item in iter_list:
            try:
                return_dict[item.name[0].upper()].append(item)
            except:
                return_dict["#"].append(item)
        return return_dict

    def get_user(self, username):
        return next((user for user in self.data.dataset_of_user if user.name == username), None)

    def add_user(self, user):
        if user not in self.data.dataset_of_user:
            self.data.dataset_of_user.append(user)
        self.data.write_user()

    def generate_user_id(self):
        return str(len(self.data.dataset_of_user))

    def get_comment(self, comment_id):
        return self.data.dataset_of_comment[int(comment_id)]

    def add_comment(self, comment):
        self.data.dataset_of_comment.append(comment)
        self.data.write_comment()
        self.data.read_comment_file()

    def generate_comment_id(self):
        return str(len(self.data.dataset_of_comment))

    def like(self, user_id, movie_id):
        self.data.dataset_of_user[int(user_id)].like(self.data.dataset_of_movie[int(movie_id)])
        self.data.write_user()

    def dislike(self, user_id, movie_id):
        self.data.dataset_of_user[int(user_id)].dislike(self.data.dataset_of_movie[int(movie_id)])
        self.data.write_user()
