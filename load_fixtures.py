import os
from contextlib import suppress

from sqlalchemy.exc import IntegrityError

from project.models import Director, Genre, Movie
from project.server import create_app
from project.setup_db import db
from project.utils.utils import read_json

app = create_app(os.getenv("FLASK_ENV", "development"))

data = read_json("fixtures.json")

with app.app_context():
    for director in data["directors"]:
        db.session.add(Director(id=director["pk"], name=director["name"]))

    for genre in data["genres"]:
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))

    for movie in data["movies"]:
        db.session.add(
            Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
        )

    with suppress(IntegrityError):
        db.session.commit()
