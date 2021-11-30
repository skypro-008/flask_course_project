from http import HTTPStatus

import pytest
from freezegun import freeze_time

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


class TestLoginUserView:
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
        assert response.status_code == HTTPStatus.OK
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

    def test_update_token_success(self, client, user, credentials):
        @freeze_time('2021-06-30T10:30:20')
        def post_response(data) -> dict:
            response = send_form_request(client, 'post', self.url, data)
            assert response.status_code == HTTPStatus.OK
            return response.json

        @freeze_time('2021-06-30T10:30:21')
        def put_response(data) -> dict:
            response = client.put(self.url, json=data)
            assert response.status_code == HTTPStatus.OK
            return response.json

        old_tokens = post_response(credentials)
        new_tokens = put_response(old_tokens)

        assert old_tokens['access_token'] != new_tokens['access_token']
        assert old_tokens['refresh_token'] != new_tokens['refresh_token']

    def test_tokens_expired(self, client, user, credentials):
        @freeze_time('2021-06-30T10:30:20')
        def post_response(data) -> dict:
            response = send_form_request(client, 'post', self.url, data)
            assert response.status_code == HTTPStatus.OK
            return response.json

        @freeze_time('2022-06-30T10:30:20')
        def put_response(data) -> dict:
            response = client.put(self.url, json=data)
            assert response.status_code == HTTPStatus.UNAUTHORIZED
            return response.json

        assert put_response(post_response(credentials)) == {'message': 'Invalid refresh token'}

    def test_invalid_refresh_token(self, client, user, credentials):
        response = client.put(self.url, json={
            'access_token': 'access_token',
            'refresh_token': 'refresh_token'
        })

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        assert response.json == {'message': 'Invalid refresh token'}
