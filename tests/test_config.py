import os

from project.config import BASEDIR
from project.server import create_app


def test_testing():
    app_config = create_app('testing').config
    assert app_config['TESTING'] is True
    assert app_config['PWD_HASH_ITERATIONS'] == 100_000
    assert app_config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'
    assert app_config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
    assert app_config['TOKEN_EXPIRE_MINUTES'] == 15
    assert app_config['TOKEN_EXPIRE_DAYS'] == 130


def test_development():
    app_config = create_app('development').config
    assert app_config['TESTING'] is False
    assert app_config['DEBUG'] is True
    assert app_config['TOKEN_EXPIRE_MINUTES'] == 5
    assert app_config['TOKEN_EXPIRE_DAYS'] == 50
    assert app_config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    assert app_config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
    assert app_config['SQLALCHEMY_ECHO'] is True


def test_production():
    app_config = create_app('production').config
    assert app_config['TESTING'] is False
    assert app_config['DEBUG'] is False
    assert app_config['TOKEN_EXPIRE_MINUTES'] == 15
    assert app_config['TOKEN_EXPIRE_DAYS'] == 130
    assert app_config['SQLALCHEMY_DATABASE_URI'] == os.getenv('DATABASE_URL')
    assert app_config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
    assert app_config['SQLALCHEMY_ECHO'] is False


def test_default():
    assert create_app('production').config == create_app('qwerty').config
