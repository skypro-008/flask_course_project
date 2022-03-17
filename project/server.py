import logging

from flask import Flask
from flask_cors import CORS

from project.config import get_config
from project.errors import BaseProjectException
from project.setup import api, db
from project.views import directors_ns, genres_ns, movies_ns

cors = CORS()


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    app.logger.setLevel(logging.DEBUG if app.config['DEBUG'] else logging.INFO)

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # api.add_namespace(auth_ns)
    api.add_namespace(directors_ns)
    # api.add_namespace(favorites_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)

    # api.add_namespace(user_ns)

    @api.errorhandler(BaseProjectException)
    def handle_validation_error(error):
        return error.message, error.code

    return app
