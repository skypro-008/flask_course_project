import json
import os

from project.models import Director, Genre, Movie
from project.server import create_app
from project.tools.setup_db import db

app = create_app(os.getenv('FLASK_ENV', 'development'))

# Read fixtures
with open('fixtures.json', encoding='utf-8') as f:
    fixtures = json.load(f)

# Load fixtures
with app.app_context():
    for director in fixtures['directors']:
        db.session.add(Director(id=director['pk'], name=director['name']))

    for genre in fixtures['genres']:
        db.session.add(Genre(id=genre['pk'], name=genre['name']))

    for movie in fixtures['movies']:
        db.session.add(Movie(
            id=movie['pk'],
            title=movie['title'],
            description=movie['description'],
            trailer=movie['trailer'],
            year=movie['year'],
            rating=movie['rating'],
            genre_id=movie['genre_id'],
            director_id=movie['director_id']
        ))

    db.session.commit()
