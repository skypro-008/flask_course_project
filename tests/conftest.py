import pytest

from project.server import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        yield app
