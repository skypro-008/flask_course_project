from http import HTTPStatus

import pytest

from project.dao import UserDAO
from project.exceptions import InvalidCredentials, UserAlreadyExists
from project.tools.security import generate_password_hash
from tests.utils import send_form_request


class TestRegisterUserView:
    url = '/auth/register'

    def test_view(self, client):
        response = send_form_request(client, 'post', self.url, {'email': 'test@example.com', 'password': 'test123'})
        assert response.status_code == HTTPStatus.CREATED
        assert response.json is None

    def test_bad_request(self, client):
        assert send_form_request(
            client, 'post', self.url, {'email': 'invalid_email_address', 'password': 'test123'}
        ).status_code == HTTPStatus.BAD_REQUEST

    def test_user_already_exists(self, db, client):
        form_data = {'email': 'test@example.com', 'password': 'test123'}

        response_1 = send_form_request(client, 'post', self.url, form_data)
        assert response_1.status_code == HTTPStatus.CREATED

        response_2 = send_form_request(client, 'post', self.url, form_data)
        assert response_2.status_code == UserAlreadyExists.code
        assert response_2.json == UserAlreadyExists.message


class LoginUserView:
    url = '/auth/login'

    @pytest.fixture
    def credentials(self):
        return {'email': 'test@test.com', 'password': 'test123'}

    @pytest.fixture
    def user(self, db, credentials):
        return UserDAO(db.session).create(
            email=credentials['email'],
            password=generate_password_hash(credentials['password'])
        )

    def test_success_login(self, client, user, credentials):
        response = send_form_request(client, 'post', self.url, credentials)
        assert response.status_code == HTTPStatus.CREATED
        assert {'access_token', 'refresh_token'} == response.json.keys()

    def test_user_not_found(self, client, credentials):
        response = send_form_request(client, 'post', self.url, credentials)
        assert response.status_code == InvalidCredentials.code
        assert response.json == InvalidCredentials.message

    def test_invalid_password(self, client, user, credentials):
        credentials['password'] = credentials['password'] * 2
        response = send_form_request(client, 'post', self.url, credentials)
        assert response.status_code == InvalidCredentials.code
        assert response.json == InvalidCredentials.message
