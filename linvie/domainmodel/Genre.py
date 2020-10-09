class Genre():
    def __init__(self, name):
        self.ID = name
        self.name = name
        self.url = " "

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, other):
        self.__ID = other

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        if other == "" or type(other) is not str:
            raise TypeError
        else:
            self.__name = other

    @property
    def type(self):
        return ["Genre"]

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_path):
        if new_path:
            self.__url = new_path

    @property
    def href(self):
        return "genre"

    def __repr__(self):
        return f"<Genre {self.name}>"

    def __eq__(self, other):
        if type(other) is Genre:
            return self.ID == other.ID
        return False

    def __lt__(self, other):
        return self.name < other.name

    def __hash__(self):
        return hash(self.name)
