import pytest

from project.dao import UserDAO
from project.models import Director, Genre, Movie
from project.server import create_app
from project.services.auth import UserSchema
from project.setup.db import db as database
from project.utils.jwt_token import JwtToken
from project.utils.security import generate_password_hash


@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.rollback()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client


@pytest.fixture
def user(db):
    return UserDAO(db.session).create(
        email="test@test.com", password=generate_password_hash("test123")
    )


@pytest.fixture
def login_headers(client, user):
    tokens = JwtToken(UserSchema().dump(user))
    return {"Authorization": f"Bearer {tokens.access_token}"}


@pytest.fixture
def genre(db):
    obj = Genre(name="genre")
    db.session.add(obj)
    db.session.commit()
    return obj


@pytest.fixture
def director(db):
    obj = Director(name="director")
    db.session.add(obj)
    db.session.commit()
    return obj


@pytest.fixture
def movies(db, genre, director):
    movies_list = []
    for i in range(10):
        obj = Movie(
            title=f"title_{i}",
            description=f"description_{i}",
            year=2000 + i,
            genre_id=genre.id,
            director_id=director.id,
        )
        db.session.add(obj)
        db.session.flush()
        movies_list.append(obj)
    db.session.commit()
    return movies_list
