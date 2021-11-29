import pytest
from marshmallow.exceptions import ValidationError

from project.models import User
from project.services.auth import RegisterNewUserService


def test_execute(db):
    RegisterNewUserService(db.session).execute(
        email='test@test.ru',
        password='q1w2e3R$',
        role='соискатель'
    )
    user = db.session.query(User).filter(User.email == 'test@test.ru').one()
    assert user.password_hash != 'q1w2e3R$'


def test_validation_error(db):
    with pytest.raises(ValidationError):
        RegisterNewUserService(db.session).execute(**{
            'email': 'test',
            'password': 'qwerty',
            'role': 'соискатель'
        })
