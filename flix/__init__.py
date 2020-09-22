import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object("config.Config")
    data_path = os.path.join('flix', 'adapters')
    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # create repo

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

    return app
