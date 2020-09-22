


class Director:

    def __init__(self, director_full_name: str):
        self.name=director_full_name
        self.directed=[]

    @property
    def directed(self):
        return self.__directed
    @directed.setter
    def directed(self,direct):
        if type(direct) is list:
            self.__directed=direct

    def is_director_of(self,movie):

        if movie not in self.directed:
            self.directed.append(movie)


    @property
    def name(self) -> str:
        return self.__director_full_name
    @name.setter
    def name(self,other):
        if other == "" or type(other) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = other.strip()

    def __repr__(self):
        return f"<Director {self.name}>"

    def __eq__(self, other):
        if type(other) is Director:
            return self.name==other.name
        return False

    def __lt__(self, other):
        if type(other) is Director:
            return self.name < other.name

    def __hash__(self):
        return hash(self.name)
