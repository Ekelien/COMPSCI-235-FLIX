


class Actor:
    def __init__(self, fullname):

        self.colleagues = []
        # films the actor participate in
        self.participating = []

    @property
    def participating(self):
        return self.__participating

    @participating.setter
    def participating(self, participate):
        if type(participate) is list:
            self.__participating = participate
        else:
            raise TypeError

    def participate_in(self, movie):
        if movie not in self.participating:
            self.participating.append(movie)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        if other != "" and type(other) is str:
            self.__name = other.strip()
        else:
            raise TypeError

    def __repr__(self):
        return f"<Actor {self.name}>"

    def __eq__(self, other):
        if type(other) is Actor:
            return self.actor_full_name == other.actor_full_name
        return False

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            self.colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if type(colleague) is Actor:
            return colleague in self.colleagues
        return False
