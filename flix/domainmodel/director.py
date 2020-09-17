


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
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if type(other) is Director:
            return self.director_full_name==other.director_full_name
        return False

    def __lt__(self, other):
        if type(other) is Director:
            return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def test_other(self):
        d1=Director("Fuck")
        d2=Director("Fuck")
        assert (d1==d2) == True
        assert (d1==3) == False
        assert hash(d1)== hash(d1.director_full_name)
        d3=Director("Gui")
        ls=[d3,d1,d2]
        ls.sort()
        assert (ls[2]==d3) == True