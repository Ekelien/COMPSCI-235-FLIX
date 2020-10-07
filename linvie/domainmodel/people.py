from linvie.domainmodel.movie import Movie


class People:


    def __init__(self, name):
        self.__url = ""
        self.name = name
        self.movie_participated = []  # active if people is actor
        self.movie_directed = []  # active if people is director
        self.occupation = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        if other != "" and type(other) is str:
            self.__name = other.strip()
        else:
            raise TypeError

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_path):
        if new_path:
            self.__url = new_path


    @property
    def type(self):
        return self.occupation

    @property
    def href(self):
        return "people"

    # judge occupation
    def if_is_actor(self):
        return "Actor" in self.occupation

    def if_is_director(self):
        return "Director" in self.occupation

    # setting occupation
    def is_actor(self):
        if self.if_is_actor():
            return
        self.occupation.append("Actor")

    def is_director(self):
        if self.if_is_director():
            return
        self.occupation.append("Director")

    def participate_in(self, movie):
        if type(movie) is Movie and movie not in self.movie_participated:
            self.movie_participated.append(movie)

    def direct(self, movie):
        if type(movie) is Movie and movie not in self.movie_directed:
            self.movie_directed.append(movie)

    def __lt__(self, other):
        return self.name<other.name

    def __eq__(self, other):
        return self.name==other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        occupation=", ".join(self.occupation)
        return f"{self.name}: {occupation} <Direct: {len(self.movie_directed)}> <Participate: {len(self.movie_participated)}>"
