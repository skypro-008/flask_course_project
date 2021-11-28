from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.config import get_config

db = SQLAlchemy()


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    db.init_app(app)

    return app
