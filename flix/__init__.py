import os

from flask import Flask
import flix.adapters.repository as repo
from flix.adapters.flix_repository import FlixRepository

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object("config.Config")

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # create repo
    repo.database=FlixRepository()

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

    return app
