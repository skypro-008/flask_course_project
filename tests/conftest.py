import pytest

from project.server import create_app, db as database


@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.rollback()
