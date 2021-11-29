import pytest

from project.dao import UserDAO
from project.exceptions import UserAlreadyExists
from project.models import User
from project.tools.enums import UserRole


def test_create(db):
    assert not db.session.query(User).all()
    data = {'email': 'test@test.com', 'password_hash': 'password_hash', 'role': UserRole.employer}
    new_user = UserDAO(db.session).create(**data)
    assert new_user.email == data['email']
    assert new_user.password_hash == data['password_hash']
    assert new_user.name is None
    assert new_user.surname is None
    assert new_user.role == data['role']
    assert User.query.get(new_user.id) == new_user


def test_create_all_fields(db):
    assert not db.session.query(User).all()
    data = {
        'email': 'test@test.com',
        'password_hash': 'password_hash',
        'role': UserRole.employer,
        'name': 'name',
        'surname': 'surname',
    }
    new_user = UserDAO(db.session).create(**data)
    assert new_user.email == data['email']
    assert new_user.password_hash == data['password_hash']
    assert new_user.name == data['name']
    assert new_user.surname == data['surname']
    assert new_user.role == data['role']
    assert User.query.get(new_user.id) == new_user


def test_create_user_with_existing_email(db):
    data = {'email': 'test@test.com', 'password_hash': 'password_hash', 'role': UserRole.employer}
    with pytest.raises(UserAlreadyExists):
        for _ in range(2):
            UserDAO(db.session).create(**data)
