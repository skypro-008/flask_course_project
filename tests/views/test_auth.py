from http import HTTPStatus

import pytest

from project.exceptions import UserAlreadyExists
from project.tools.enums import UserRole


class TestRegisterUser:
    valid_data = {
        'email': 'new_user@email.com',
        'password': 'test1234',
        'role': UserRole.employer.value
    }

    def collect_data(self, email=None, password=None, role=None):
        return f"email={email}&password={password}&role={role}"

    def register_user(self, test_client, data):
        return test_client.post(
            '/auth/register', data=data,
            content_type="application/x-www-form-urlencoded",
        )

    def test_view(self, client):
        response = self.register_user(client, self.collect_data(**self.valid_data))
        assert response.status_code == HTTPStatus.CREATED
        assert response.json is None

    @pytest.mark.parametrize('data', (
        {'email': 'test'},
        {'role': 'some_role'},
    ))
    def test_bad_request(self, client, data):
        valid_data = self.valid_data.copy()
        valid_data.update(data)
        response = self.register_user(client, self.collect_data(**valid_data))
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_user_already_exists(self, db, client):
        self.register_user(client, self.collect_data(**self.valid_data))
        response = self.register_user(client, self.collect_data(**self.valid_data))
        assert response.status_code == HTTPStatus.CONFLICT
        assert response.json == {'message': UserAlreadyExists.message}
