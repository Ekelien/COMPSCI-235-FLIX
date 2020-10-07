from flask import Flask
import linvie.adapters.repository as repo
from linvie.adapters.flix_repository import FlixRepository
from linvie.adapters.user_repository import UserRepository


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object("config.Config")

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # create repo
    repo.database=FlixRepository()
    repo.users=UserRepository()

    with app.app_context():
        from .blueprint import home
        from linvie.blueprint.General import index
        from linvie.blueprint.MovieObject import people
        from linvie.blueprint.MovieObject import movie
        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(people.people_blueprint)
        app.register_blueprint(movie.movie_blueprint)
        app.register_blueprint(index.index_blueprint)

    return app
