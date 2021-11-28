import pytest
from marshmallow import ValidationError

from project.dao import UserDAO
from project.enums import UserRole
from project.models import User


def test_create(db):
    assert not db.session.query(User).all()
    data = {'email': 'test@test.com', 'password': 'password', 'role': UserRole.employer}
    new_user = UserDAO(db.session).create(**data)
    assert new_user.email == data['email']
    assert new_user.password_hash != data['password']
    assert new_user.name is None
    assert new_user.surname is None
    assert new_user.role == data['role']
    assert User.query.get(new_user.id) == new_user


def test_create_all_fields(db):
    assert not db.session.query(User).all()
    data = {
        'email': 'test@test.com',
        'password': 'password',
        'role': UserRole.employer,
        'name': 'name',
        'surname': 'surname',
    }
    new_user = UserDAO(db.session).create(**data)
    assert new_user.email == data['email']
    assert new_user.password_hash != data['password']
    assert new_user.name == data['name']
    assert new_user.surname == data['surname']
    assert new_user.role == data['role']
    assert User.query.get(new_user.id) == new_user


@pytest.mark.parametrize('data', [
    {'email': 'test', 'password': 'password', 'role': UserRole.employer},
    {'email': 'test@test.com', 'role': UserRole.employer},
    {'email': 'test@test.com', 'password': 'password', 'role': ''},
])
def test_create_invalid_fields(db, data):
    assert not db.session.query(User).all()
    with pytest.raises(ValidationError):
        UserDAO(db.session).create(**data)
