# pytest file
import csv
import pytest

from linvie.domainmodel.genre import Genre
from linvie.domainmodel.movie import Movie
from linvie.domainmodel.user import User
from linvie.domainmodel.recommended import RecommendedWatchList

csv_file = open("..\\datafiles\\Data1000Movies.csv", encoding='utf-8')
csv_reader = csv.DictReader(csv_file)
movie_list=[]
counter=0
for row in csv_reader:
    temp = dict(row)
    movie = Movie(temp['Title'], temp['Year'])
    for i in temp['Genre'].split(","):
        genre = Genre(i.strip())
        movie.add_genre(genre)
    movie_list.append(movie)
    counter+=1
    if counter>10:
        break
    # read the first 10 movie from csv

recommend=RecommendedWatchList()


def test_print_10_movie():
    for i in movie_list:
        print(i, i.genres)

def test_user_name_pass():
    user = User("Trump", "twitterking")
    assert user.user_name=="trump"
    assert user.password=="twitterking"

def test_preference_adding_correctly():
    user = User("Trump", "twitterking")
    movie=Movie("ooo",9999)
    movie.add_genre(Genre("onmygod"))
    user.add_preference(Genre("Action"))
    user.add_preference(Genre("Sci-Fi"))
    user.watch_movie(movie)
    ls=[Genre("onmygod"),Genre("Action"),Genre("Sci-Fi")]
    assert ls.sort()==recommend.get_user_preference(user).sort()


def test_preference_by_watching():
    user = User("Trump", "twitterking")
    user.watch_movie(movie_list[0])
    indicator=0
    for movie in recommend.get_recommended_watch_list(user):
        for genre in movie.genres:
            if genre in recommend.get_user_preference(user):
                indicator+=1
        assert  indicator > 0 # all movie is linked to preference
        indicator=0

def test_preference_by_preference():
    user = User("Trump", "twitterking")
    user.add_preference(Genre("Action"))
    user.add_preference(Genre("Sci-Fi"))
    assert  user.preference.sort()==recommend.get_user_preference(user).sort()
    indicator = 0
    for movie in recommend.get_recommended_watch_list(user):
        for genre in movie.genres:
            if genre in recommend.get_user_preference(user):
                indicator += 1
        assert indicator > 0  # all movie is linked to preference
        indicator = 0

def test_multiple_way():
    user = User("Trump", "twitterking")
    pref=[Genre("Crime")]
    for i in movie_list:
        user.watch_movie(i)
        for genre in i.genres:
            if genre not in pref:
                pref.append(genre)
    user.add_preference(Genre("Crime"))# not a genre of first 10 movie
    indicator = 0
    indicator2 = 0
    for movie in recommend.get_recommended_watch_list(user,10): #get 10 movie
        for genre in movie.genres:
            if genre in pref:
                indicator += 1
            if genre == Genre("Crime"):
                indicator2 +=1
        assert indicator > 0  # all movie is linked to preference
    assert indicator2 != 0


# def special():
#     user = User("Trump", "twitterking")
#     pref = [Genre("Crime")]
#     for i in movie_list:
#         user.watch_movie(i)
#         for genre in i.genres:
#             if genre not in pref:
#                 pref.append(genre)
#     user.add_preference(Genre("Crime"))  # not a genre of first 10 movie
#     indicator = 0
#     indicator2 = 0
#     for movie in recommend.get_recommended_watch_list(user, 10):  # get 10 movie
#         for genre in movie.genres:
#             if genre in pref:
#                 indicator += 1
#             if genre == Genre("Crime"):
#                 indicator2 += 1
#     return indicator2 != 0
#
# f=0
# n=10000
# for i in range(n):
#     if special() == False:
#         f+=1
# print("{}%".format(f/n))