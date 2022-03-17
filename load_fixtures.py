import json
import os
from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from project.models import Director, Genre, Movie
from project.server import create_app
from project.setup.db import db, models

app = create_app(os.getenv("FLASK_ENV", "development"))


def read_json(filename: str, encoding: str = 'utf-8'):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def load_data(data: List[Dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    data: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    with app.app_context():
        load_data(data['directors'], Director)
        load_data(data['genres'], Genre)
        load_data(data['movies'], Movie)

        with suppress(IntegrityError):
            db.session.commit()
