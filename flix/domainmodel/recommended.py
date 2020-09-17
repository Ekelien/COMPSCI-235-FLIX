from flix.domainmodel.user import User
from flix.domainmodel.movie_csv import MovieFileCSVReader
from flix.domainmodel.movie import Movie
import random
class RecommendedWatchList:
    '''
    a recommended watchlist that based on user's watched movie and user's preference of genre
    '''
    def __init__(self):
        file = MovieFileCSVReader("..\\datafiles\\Data1000Movies.csv")
        self.movie_list_by_genre = file.get_dict_by_genre()

    def get_user_preference(self,user:User):
        user_preference = []
        if type(user) is not User:
            return
        for i in user.preference:
            user_preference.append(i)
        for i in user.watched_movies:
            for genre in i.genres:
                if genre not in user_preference:
                    user_preference.append(genre)
        return user_preference

    def get_recommended_watch_list(self,user:User,num:int=5):
        if type(user) is not User:
            return
        user_preference=self.get_user_preference(user)
        return_list=[]
        i=0
        while i<num:
            random_num=random.randrange(0,len(user_preference))
            movie_list=self.movie_list_by_genre[user_preference[random_num]]
            random_num=random.randrange(0,len(movie_list))
            if movie_list[random_num] not in return_list:
                return_list.append(movie_list[random_num])
                i+=1
        return return_list
