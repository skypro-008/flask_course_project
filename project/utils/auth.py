from functools import wraps

import jwt
from flask import abort, current_app, request


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not (authorization_header := request.headers.get('Authorization')):
            abort(401)

        access_token: str = authorization_header.split('Bearer ')[-1]

        try:
            jwt.decode(access_token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.exceptions.PyJWTError as e:
            print('JWT Decode Exception', e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper
