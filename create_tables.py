import os

from project.models import User, Director, Genre, Movie # noqa F401
from project.server import create_app
from project.tools.setup_db import db

app = create_app(os.getenv('FLASK_ENV', 'development'))

with app.app_context():
    db.drop_all()
    db.create_all()
