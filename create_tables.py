import os

from project.server import create_app
from project.setup_db import db

app = create_app(os.getenv("FLASK_ENV", "development"))

with app.app_context():
    db.create_all()
