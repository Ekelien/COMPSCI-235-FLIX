from linvie.domainmodel.movie import Movie
from linvie.domainmodel.review import Review
from linvie.domainmodel.genre import Genre


class User:
    def __init__(self, name, password):
        self.user_name = name
        self.password = password
        self.watched_movies = []
        self.preference=[]
        self.reviews = []
        self.time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__name

    @user_name.setter
    def user_name(self, other):
        if type(other) is str:
            self.__name = other.strip().lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, other):
        if type(other) is str:
            self.__password = other

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, other):
        if type(other) is list and all((type(x) is Movie) for x in other):
            self.__watched_movies = other

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, other):
        if type(other) is list and all((type(x) is Review) for x in other):
            self.__reviews = other

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, other):
        if other >= 0:
            self.__time_spent = other
            return

    @property
    def preference(self):
        return self.__preference

    @preference.setter
    def preference(self,other):
        if type(other) is list and all((type(x) is Genre) for x in other):
            self.__preference=other

    def __repr__(self):
        return f"<User {self.user_name}>"

    def __eq__(self, other):
        if type(other) is User:
            return self.user_name == other.user_name
        return False

    def __lt__(self, other):
        if type(other) is User:
            return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie):
        if type(movie) is Movie:
            if movie not in self.watched_movies:
                self.watched_movies.append(movie)
            self.time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is Review:
            self.reviews.append(review)

    def add_preference(self,other):
        if type(other) is Genre:
            if other not in self.preference:
                self.preference.append(other)

    def delete_preference(self,other):
        if type(other) is Genre:
            if other in self.preference:
                self.preference.remove(other)



