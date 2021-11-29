import pytest
from marshmallow.exceptions import ValidationError

from project.models import User
from project.services.auth import RegisterNewUserService


class TestRegisterNewUserService:

    def test_execute(self, db):
        RegisterNewUserService(db.session).execute(
            email='test@test.ru',
            password='q1w2e3R$',
        )
        user = db.session.query(User).filter(User.email == 'test@test.ru').one()
        assert user.password != 'q1w2e3R$'

    def test_validation_error(self, db):
        with pytest.raises(ValidationError):
            RegisterNewUserService(db.session).execute(
                email='test',
                password='qwerty',
            )
