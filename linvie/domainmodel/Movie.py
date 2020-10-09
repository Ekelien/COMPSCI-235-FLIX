from linvie.domainmodel.Genre import Genre


class Movie:
    def __init__(self, ID, title, year):
        self.ID = ID
        self.name = title
        self.year = year
        self.runtime_minutes = 0
        self.actors = []
        self.genres = []
        self.url = " "
        self.comments = []

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, other):
        self.__ID = other

    @property
    def name(self):
        return self.__title

    @name.setter
    def name(self, other):
        if type(other) is str:
            self.__title = other.strip()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, other):
        if type(other) is int and other < 1900:
            raise ValueError
        self.__year = other

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_path):
        if new_path:
            self.__url = new_path

    @property
    def type(self):
        return ["Movie"]

    @property
    def href(self):
        return "movie"

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, other):
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
    def actors(self, other):
        self.__actors = other

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, other):
        self.__genres = other

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, other):
        self.__director = other

    def add_actor(self, actor):
        if actor not in self.actors:
            self.actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.actors:
            self.actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) is Genre and genre not in self.genres:
            self.genres.append(genre)

    def remove_genre(self, genre):
        if type(genre) is Genre and genre in self.genres:
            self.genres.remove(genre)

    def __repr__(self):
        return f"<Movie {self.name}>"

    def __eq__(self, other):
        return self.ID == other.ID

    def __lt__(self, other):
        return self.name + str(self.year) < other.name + str(other.year)

    def __hash__(self):
        return hash(self.name + str(self.year))

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, other):
        self.__comments = other

    def add_comment(self, review):
        if review not in self.comments:
            self.comments.append(review)
