from linvie.domainmodel.genre import Genre
from linvie.domainmodel.actor import Actor
from linvie.domainmodel.director import Director


class Movie:
    def __init__(self, title, year):
        self.name = title
        self.time = year
        self.runtime_minutes=0
        self.actors = []
        self.genres = []
        self.url=""

    @property
    def name(self):
        return self.__title

    @name.setter
    def name(self, other):
        if type(other) is str:
            self.__title = other.strip()

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, other):
        if type(other) is int and other < 1900:
            raise ValueError
        self.__time = other

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self,new_path):
        if new_path:
            self.__url=new_path
            return
        self.__url=""

    @property
    def type(self):
        return "Movie"

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, other):
        if type(other) is str:
            self.__description = other.strip()

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, other):
        if type(other) is int and other >= 0:
            self.__runtime_minutes = other
        else:
            raise ValueError

    @property
    def actors(self):
        return self.__actors
    @actors.setter
    def actors(self,other):
        if type(other) is list and all(isinstance(x, Actor) for x in other):
            self.__actors=other

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, other):
        if type(other) is list and all(isinstance(x, Genre) for x in other):
            self.__genres = other

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self,other):
        self.__director=other

    @property
    def href(self):
        return "movie"

    def __repr__(self):
        return f"<Movie {self.name}, {self.time}><Director {self.director}><Actors {self.actors}>"

    def __eq__(self, other):
        return self.name +str(self.time) == other.name+ str(other.time)

    def __lt__(self, other):
        return self.name +str(self.time) < other.name+ str(other.time)

    def __hash__(self):
        return hash(self.name +str(self.time))

    def add_actor(self, actor):
        if actor not in self.actors:
            self.actors.append((actor))

    def remove_actor(self, actor):
        if actor in self.actors:
            self.actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) is Genre and genre not in self.genres:
            self.genres.append((genre))

    def remove_genre(self, genre):
        if type(genre) is Genre and genre in self.genres:
            self.genres.remove(genre)