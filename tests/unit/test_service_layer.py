from TEST_DATA_PATH import PATH
from linvie import Repository
from linvie.adapters import AbstractRepository as repo
from linvie.blueprint.UserService import service

repo.db = Repository(movie_file_path=PATH + "\\movie.csv", user_file_path=PATH + "\\user.csv",
                     comment_file_path=PATH + "\\comments.csv")


def test_get_user():
    user = service.get_user('ekelien', repo)
    assert user.name == 'ekelien'
    assert len(user.favorite) == 2


def test_add_user():
    service.add_user('haly', '6666', repo)
    user = service.get_user('haly', repo)
    assert user.name == 'haly'
    repo.db.data.dataset_of_user.pop(-1)
    repo.db.data.write_user()


def test_add_user_with_exist_name():
    try:
        service.add_user('ekelien', 'momomomomo', repo)
        assert False
    except:
        assert True


def test_add_get_comment():
    service.add_comment(0, 'ekelien', 'good!', repo)
    comment = service.get_comment(1, repo)
    assert comment.comment_text == 'good!'
    repo.db.data.dataset_of_comment.pop(-1)
    repo.db.data.write_comment()


def test_like_a_movie():
    service.add_user('haly', '6666', repo)
    user = service.get_user('haly', repo)
    service.like('0', 'haly', repo)
    assert len(user.favorite) == 1
    assert user.favorite[0].ID == '0'
    repo.db.data.dataset_of_user.pop(-1)
    repo.db.data.write_user()


def test_dislike_a_movie():
    service.add_user('haly', '6666', repo)
    user = service.get_user('haly', repo)
    service.like('0', 'haly', repo)
    assert len(user.favorite) == 1
    assert user.favorite[0].ID == '0'
    service.dislike('0', 'haly', repo)
    assert len(user.favorite) == 0
    repo.db.data.dataset_of_user.pop(-1)
    repo.db.data.write_user()
