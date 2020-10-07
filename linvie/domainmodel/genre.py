

class Genre:
    def __init__(self,name):
        if name=="" or type(name) is not str:
            self.__name=None
        else:
            self.__name=name
        self.__url = ""
    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"<Genre {self.name}>"

    def __eq__(self, other):
        if type(other) is Genre:
            return self.name==other.name
        return False

    def __lt__(self, other):
        return self.name<other.name

    def __hash__(self):
        return hash(self.name)

    @property
    def href(self):
        return "genre"

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_path):
        if new_path:
            self.__url = new_path