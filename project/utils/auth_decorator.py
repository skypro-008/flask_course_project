from contextlib import suppress
from functools import wraps

import jwt
from flask import current_app, request
from jwt import PyJWTError

from project.errors import AuthenticationError


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if authorization_header := request.headers.get('Authorization'):

            with suppress(PyJWTError):
                if user_id := jwt.decode(
                    jwt=authorization_header.split('Bearer ')[-1],
                    key=current_app.config['SECRET_KEY'],
                    algorithms=['HS256'],
                ).get('id'):
                    return func(user_id=user_id, *args, **kwargs)

        raise AuthenticationError

    return wrapper
