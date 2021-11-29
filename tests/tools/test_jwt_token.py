from datetime import datetime

import pytest
from freezegun import freeze_time
from jwt.exceptions import PyJWTError

from project.tools.jwt_token import JwtToken


@freeze_time('2021-06-30T10:30:20')
def test_jwt_token(app):
    data = {'name': 'username'}
    token = JwtToken(data)
    assert token._now == datetime.fromisoformat('2021-06-30T10:30:20')

    assert JwtToken.decode_token(token.access_token) == data
    assert JwtToken.decode_token(token.refresh_token) == data


def test_decoding_error(app):
    with pytest.raises(PyJWTError):
        JwtToken.decode_token('bad_token')


@freeze_time('2021-06-30T10:30:20')
def test_token_expired(app):
    token = JwtToken({})
    token._now = datetime.fromisoformat('2020-06-30T10:30:20')
    with pytest.raises(PyJWTError):
        assert JwtToken.decode_token(token.access_token)
