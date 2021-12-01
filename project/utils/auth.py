from functools import wraps

import jwt
from flask import abort, current_app, request
from jwt import PyJWTError


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not (authorization_header := request.headers.get('Authorization')):
            abort(401)

        access_token: str = authorization_header.split('Bearer ')[-1]

        try:
            user_id = jwt.decode(access_token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['id']
            return func(user_id=user_id, *args, **kwargs)
        except (PyJWTError, KeyError):
            abort(401)

    return wrapper
