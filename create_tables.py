import os

from project.server import create_app
from project.setup.db import db

if __name__ == '__main__':
    with create_app(os.getenv("FLASK_ENV", "development")).app_context():
        db.create_all()
