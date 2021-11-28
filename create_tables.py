import os

from project.models import User  # noqa F401
from project.server import create_app, db

app = create_app(os.getenv('FLASK_ENV', 'development'))

with app.app_context():
    db.create_all()
