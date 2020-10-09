from flask import Flask

import linvie.adapters.AbstractRepository as repo
from TEST_DATA_PATH import PATH
from linvie.adapters.Repository import Repository


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object("config.Config")

    # create repo

    if test_config:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        repo.db = Repository(movie_file_path=PATH + "\\movie.csv", user_file_path=PATH + "\\user.csv",
                             comment_file_path=PATH + "\\comments.csv")
    else:
        repo.db = Repository()

    with app.app_context():
        from .blueprint import home
        from linvie.blueprint.General import index
        from linvie.blueprint.MovieObject import people
        from linvie.blueprint.MovieObject import movie
        from linvie.blueprint.UserService import User
        from linvie.blueprint.MovieObject import genre
        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(people.people_blueprint)
        app.register_blueprint(movie.movie_blueprint)
        app.register_blueprint(index.index_blueprint)
        app.register_blueprint(User.user_blueprint)
        app.register_blueprint(genre.genre_blueprint)

    return app
