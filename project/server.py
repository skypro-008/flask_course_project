from flask import Flask
from flask_restx import Api

from project.config import get_config
from project.views.auth import auth_ns
from project.tools.setup_db import db

api = Api()


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    db.init_app(app)
    api.init_app(app)

    api.add_namespace(auth_ns)

    return app
