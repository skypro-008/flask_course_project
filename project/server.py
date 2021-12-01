import logging

from flask import Flask
from flask_restx import Api

from project.config import get_config
from project.tools.exceptions import BaseProjectException
from project.tools.setup_db import db
from project.views import auth_ns, directors_ns, genres_ns, movies_ns, user_ns

api = Api(
    authorizations={
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    title='Flask API',
    description='Welcome to the Swagger UI documentation site!',
    doc='/ui'
)


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    app.logger.setLevel(logging.DEBUG if app.config['DEBUG'] else logging.INFO)

    db.init_app(app)
    api.init_app(app)

    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)

    @api.errorhandler(BaseProjectException)
    def handle_validation_error(error):
        return error.message, error.code

    return app
