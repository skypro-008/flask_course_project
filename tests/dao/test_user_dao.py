import pytest
from marshmallow import ValidationError

from project.dao import UserDAO
from project.exceptions import UserAlreadyExists
from project.models import User


class TestUserDAO:
    def test_create_user(self, db):
        assert not db.session.query(User).all()

        data = {'email': 'test@test.com', 'password': 'password_hash'}
        new_user = UserDAO(db.session).create(**data)

        assert new_user.email == data['email']
        assert new_user.password == data['password']
        assert new_user.name is None
        assert new_user.surname is None
        assert User.query.get(new_user.id) == new_user

    def test_create_user_with_existing_email(self, db):
        with pytest.raises(UserAlreadyExists):
            for _ in range(2):
                UserDAO(db.session).create(
                    email='test@test.com',
                    password='password'
                )

    def test_validation_error(self, db):
        with pytest.raises(ValidationError):
            UserDAO(db.session).create(
                email='test',
                password='qwerty',
            )
