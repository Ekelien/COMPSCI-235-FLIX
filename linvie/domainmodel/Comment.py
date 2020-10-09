from linvie.domainmodel.Time import TimeStamp


class Comment:
    def __init__(self, ID, user_id, movie_id, comment_text, time=TimeStamp.current_time()):
        self.__ID = ID
        self.user_id = user_id
        self.movie_id = movie_id
        self.comment_text = comment_text
        self.time = time

        self.user = None
        self.movie = None

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, other):
        self.__ID = other

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, other):
        self.__user_id = other

    @property
    def movie_id(self):
        return self.__movie_id

    @movie_id.setter
    def movie_id(self, other):
        self.__movie_id = other

    @property
    def comment_text(self):
        return self.__comment_text

    @comment_text.setter
    def comment_text(self, other):
        self.__comment_text = other.strip()

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, other):
        self.__time = other

    def renew(self, new_comment):
        self.comment_text = new_comment
        self.time = TimeStamp.current_time()

    def __repr__(self):
        return ""

    def __eq__(self, other):
        return self.ID == other.ID
