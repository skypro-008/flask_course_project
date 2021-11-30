import pytest

from project.dao import UserDAO
from project.server import create_app
from project.tools.setup_db import db as database
from project.utils.jwt_token import JwtToken
from project.utils.security import generate_password_hash


@pytest.fixture
def app():
    app = create_app('testing')
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
        email='test@test.com',
        password=generate_password_hash('test123')
    )


@pytest.fixture
def login_headers(client, user):
    access_token = JwtToken({}).access_token
    return {'Authorization': f'Bearer {access_token}'}
