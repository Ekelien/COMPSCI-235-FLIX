from TEST_DATA_PATH import PATH
from linvie import Repository
from linvie.adapters import AbstractRepository as repo

repo.db = Repository(movie_file_path=PATH + "\\movie.csv", user_file_path=PATH + "\\user.csv",
                     comment_file_path=PATH + "\\comments.csv")


def test_csv_reader():
    assert len(repo.db.data.dataset_of_genre.keys()) == 20
    assert len(repo.db.data.dataset_of_movie) == 1002
    assert len(repo.db.data.dataset_of_actors) == 1990
    assert len(repo.db.data.dataset_of_director) == 222
    assert len(repo.db.data.dataset_of_comment) == 1
    assert len(repo.db.data.dataset_of_people) == 2598
    assert len(repo.db.data.dataset_of_user) == 2


def test_find_movie_by_id():
    movie = repo.db.find_movie('0')
    assert movie.name == 'Shiranui'


def test_find_people():
    people = repo.db.find_people("Alexi Pappas")
    assert people.name == "Alexi Pappas"
    assert people == people.movie_directed[0].director
    assert people in people.movie_participated[0].actors
    assert 'Actor' in people.occupation
    assert 'Director' in people.occupation


def test_find_people_name_within():
    match, similar = repo.db.find("Alexi")
    people = repo.db.find_people("Alexi Pappas")
    assert people in similar


def test_find_people_name_similar():
    match, similar = repo.db.find("Alexy Papas")
    people = repo.db.find_people("Alexi Pappas")
    assert people in similar


def test_find_movie_name():
    match, similar = repo.db.find("shiranui")
    assert repo.db.find_movie('0') in match


def test_find_movie_name_similar():
    match, similar = repo.db.find("shirani")
    assert repo.db.find_movie('0') in similar


def test_user_read():
    user = repo.db.get_user('ekelien')
    assert user.ID == '0'
    assert user.name == 'ekelien'
    assert len(user.favorite) == 2
    assert repo.db.find_movie(0) in user.favorite


def test_comment_read():
    comment = repo.db.get_comment(0)
    assert comment.comment_text == "fantastic"
    assert comment.user_id == '0'
    assert repo.db.find_movie(0) == repo.db.find_movie(comment.movie_id)
