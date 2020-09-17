from datetime import datetime

from flix.domainmodel.movie import Movie



class Review:
    def __init__(self, movie=None, review_text="", rating=None):
        self.movie: Movie = movie
        self.review_text= review_text
        self.rating: int = rating
        self.__timestamp = datetime.today()

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, other):
        if type(other) is Movie:
            self.__movie = other

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, other):
        if type(other) is str:
            self.__review_text = other.strip()
            return
        self.__review_text=None

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, other):
        if type(other) is int and 0 < other < 11:
            self.__rating = other
            return
        self.__rating=None

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, other):
        pass

    def __repr__(self):
        return "{}\nReview: {}\nRating: {}".format(self.movie,self.review_text,self.rating)

    # def __repr__(self):
    #     return f"{self.movie}\nReview: {self.review_text}\nRating: {self.rating}"

    def __eq__(self, other):
        return self.movie == other.movie and self.review_text == other.review_text and self.rating == other.rating and self.timestamp == other.timestamp

