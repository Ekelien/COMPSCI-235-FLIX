from linvie.domainmodel.Movie import Movie


class User:
    def __init__(self, ID, name, password):
        self.ID = ID
        self.name = name
        self.password = password
        self.watched_movies = []
        self.comments = []
        self.time_spent_watching_movies_minutes = 0
        self.__favorite = []

    @property
    def ID(self):
        return self.__id

    @ID.setter
    def ID(self, other):
        self.__id = other

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
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
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, other):
        self.__comments = other

    def __repr__(self):
        return f"<User {self.name}>"

    def __eq__(self, other):
        if type(other) is User:
            return self.ID == other.ID
        return False

    def __lt__(self, other):
        if type(other) is User:
            return self.name < other.name

    def __hash__(self):
        return hash(self.name)

    @property
    def favorite(self):
        return self.__favorite

    def like(self, movie):
        if movie not in self.__favorite:
            self.__favorite.append(movie)

    def dislike(self, movie):
        if movie in self.__favorite:
            self.__favorite.remove(movie)

    def add_comment(self, review):
        if review not in self.comments:
            self.comments.append(review)

    @property
    def preference(self):
        pref = []
        for movie in self.favorite:
            for gen in movie.genres:
                if gen not in pref:
                    pref.append(gen)
        return pref
