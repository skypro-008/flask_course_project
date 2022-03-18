import os

import pytest

from project.utils.security import generate_password_hash


class TestUserProfileView:
    url = "/user/"

    def test_unauthorized(self, user, client):
        assert client.get(self.url).status_code == 401

    def test_get_profile_success(self, user, client, login_headers):
        response = client.get(self.url, headers=login_headers)
        assert response.status_code == 200
        assert response.json == {
            "email": user.email,
            "favourite_genre": None,
            "id": user.id,
            "name": None,
            "surname": None,
        }

    @pytest.mark.parametrize(
        "data, new_data",
        [
            ({"name": "Ivan", "surname": None}, None),
            ({"name": "", "age": 10}, None),
            ({"name": "Ivan"}, {"name": "Oleg"}),
        ],
    )
    def test_update_user_data(self, data, new_data, user, client, login_headers):
        response = client.patch(self.url, json=data, headers=login_headers)
        assert response.status_code == 200
        assert response.json["name"] == (data["name"] if data["name"] else None)
        if new_data:
            response = client.patch(self.url, json=new_data, headers=login_headers)
            assert response.json["name"] != data["name"]


class TestChangePasswordView:
    url = "/user/password/"

    def test_change_password(self, db, user, client, login_headers):
        old_password = os.urandom(10).hex()
        db.session.refresh(user)
        user.password = generate_password_hash(old_password)

        new_password = os.urandom(10).hex()

        response = client.put(
            self.url,
            headers=login_headers,
            json={"old_password": old_password, "new_password": new_password},
        )
        assert response.status_code == 200
        assert not response.json

        db.session.refresh(user)
        assert user.password == generate_password_hash(new_password)

    def test_invalid_passwords(self, db, user, client, login_headers):
        response = client.put(
            self.url,
            headers=login_headers,
            json={"old_password": "123", "new_password": "321"},
        )
        assert response.status_code == 400
