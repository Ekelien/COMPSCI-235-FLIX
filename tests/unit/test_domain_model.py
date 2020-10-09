from linvie.domainmodel.Comment import Comment
from linvie.domainmodel.Genre import Genre
from linvie.domainmodel.Movie import Movie
from linvie.domainmodel.People import People
from linvie.domainmodel.User import User

director = People("Marvel")
director.is_actor()
director.is_director()
actor1 = People("Tony Stack")
actor1.is_actor()
actor2 = People("Thor")
actor2.is_actor()
movie = Movie(999, "Avengers", 2099)
movie.add_genre(Genre("soso"))
movie.add_genre(Genre("so"))
movie.add_genre(Genre("soso"))
movie.add_actor(actor1)
movie.add_actor(actor2)
movie.add_actor(director)
movie.director = director
actor1.participate_in(movie)
actor2.participate_in(movie)
director.direct(movie)
director.participate_in(movie)
print(movie.genres)

user = User(0, 'superman', '6666')
comment = Comment(0, 0, 999, 'suck movie', '09/09/09')

user.like(movie)


def test_people():
    assert director.if_is_director() == True
    assert director.if_is_actor() == True
    assert actor1.if_is_actor() == True
    assert actor2.if_is_actor() == True
    assert movie in actor1.movie_participated
    assert movie in director.movie_participated
    assert movie in director.movie_directed


def test_movie():
    assert movie.ID == 999
    assert len(movie.actors) == 3
    assert len(movie.genres) == 2
    assert actor1 in movie.actors
    assert actor2 in movie.actors
    assert director in movie.actors
    assert director == movie.director
    assert len(movie.comments) == 0
    movie.add_comment(comment)
    assert len(movie.comments) == 1


def test_user():
    assert user.ID == 0
    assert len(user.comments) == 0
    user.add_comment(comment)
    assert len(user.comments) == 1
    assert len(user.favorite) == 1
    user.dislike(movie)
    assert len(user.favorite) == 0


def test_comment():
    assert comment.ID == 0
    assert movie.ID == comment.movie_id
    assert user.ID == comment.user_id
    assert comment.comment_text == 'suck movie'
    old_time = comment.time
    comment.renew('good movie')
    assert comment.comment_text == 'good movie'
    assert comment.time != old_time
