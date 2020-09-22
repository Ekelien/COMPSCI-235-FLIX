import pytest
from flix.adapters.repository import FlixRepository
from flix.domainmodel.director import Director
from flix.domainmodel.actor import Actor
from flix.domainmodel.genre import Genre
import os

from flix.domainmodel.movie import Movie

repo = FlixRepository("../flix/data/Data1000Movies.csv")

'''test search with the keyword that 100% same as the result'''


def test_search_actor_100_same():
    search_list = repo.find("Ryan Gosling")  # Actor
    assert len(search_list) == 1
    assert type(search_list[0]) is Actor
    assert search_list[0].name == "Ryan Gosling"


def test_search_movie_100_same():
    search_list = repo.find("Guardians of the Galaxy")  # Movie
    assert len(search_list) == 1
    assert type(search_list[0]) == Movie
    assert search_list[0].name == "Guardians of the Galaxy"


def test_search_director_100_same():
    search_list = repo.find("Kenneth Lonergan")  # Director
    assert len(search_list) == 1
    assert type(search_list[0]) == Director
    assert search_list[0].name == "Kenneth Lonergan"


'''test search with keyword that is similar to result'''


def test_search_actor_similar():
    search_list = repo.find("Ryan Golin")  # Actor
    assert len(search_list) != 0  # find somthing
    for item in search_list:
        if item.name == "Ryan Gosling":  # if found means I have the search result
            assert type(item) is Actor
        else:
            assert 1 == 0  # otherwise error


def test_search_movie_similar():
    search_list = repo.find("GuARDans of Galaxy")  # Movie
    assert len(search_list) != 0  # find somthing
    for item in search_list:
        if item.name == "Guardians of the Galaxy":  # if found means I have the search result
            assert type(item) is Movie
        else:
            assert 1 == 0  # otherwise error


def test_search_director_similar():
    search_list = repo.find("KENETH Lonergan")  # Director
    assert len(search_list) != 0  # find somthing
    for item in search_list:
        if item.name == "Kenneth Lonergan":  # if found means I have the search result
            assert type(item) is Director
        else:
            assert 1 == 0  # otherwise error


'''test movie filter by genre, year'''


def test_filter_all_movie():
    filter_list = repo.movie_filter()
    assert len(filter_list) == len(repo.data.dataset_of_movie)


def test_only_genre():
    filter_list = repo.movie_filter(genre=[Genre("Sci-Fi")])
    for item in filter_list:
        assert Genre("Sci-Fi") in item.genres


def test_only_start_year():
    filter_list = repo.movie_filter(start_year=2015)
    for item in filter_list:
        assert int(item.time) >= 2015


def test_only_end_year():
    filter_list = repo.movie_filter(end_year=1999)
    for item in filter_list:
        assert int(item.time) <= 2015


def test_with_year_range():
    filter_list = repo.movie_filter(start_year=2013, end_year=2015)
    for item in filter_list:
        assert 2013 <= int(item.time) <= 2015


def test_with_all_restriction():
    filter_list = repo.movie_filter(genre=[Genre("Sci-Fi")], start_year=2000, end_year=2013)
    for item in filter_list:
        assert Genre("Sci-Fi") in item.genres
        assert 2000 <= int(item.time) <= 2013
