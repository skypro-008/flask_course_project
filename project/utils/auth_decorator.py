# from contextlib import suppress
# from functools import wraps
#
# import jwt
# from flask import abort, current_app, request
# from jwt import PyJWTError
#
#
# def login_required(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if not (authorization_header := request.headers.get('Authorization')):
#             abort(401)
#
#         with suppress(PyJWTError):
#             if user_id := jwt.decode(
#                 jwt=authorization_header.split('Bearer ')[-1],
#                 key=current_app.config['SECRET_KEY'],
#                 algorithms=['HS256'],
#             ).get('id'):
#                 return func(user_id=user_id, *args, **kwargs)
#
#         abort(401)
#
#     return wrapper
