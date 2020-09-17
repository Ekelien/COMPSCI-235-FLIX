

class Genre:
    def __init__(self,name):
        if name=="" or type(name) is not str:
            self.__genre_name=None
        else:
            self.__genre_name=name
    @property
    def genre_name(self):
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.genre_name}>"

    def __eq__(self, other):
        if type(other) is Genre:
            return self.genre_name==other.genre_name
        return False

    def __lt__(self, other):
        return self.genre_name<other.genre_name

    def __hash__(self):
        return hash(self.genre_name)