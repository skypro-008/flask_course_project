from http import HTTPStatus as status
from typing import Dict


class BaseProjectException(Exception):
    _message: str = 'Something went wrong'
    code: int = status.INTERNAL_SERVER_ERROR

    @classmethod
    @property
    def message(cls) -> Dict[str, str]:
        return {'message': cls._message}


class UserAlreadyExists(BaseProjectException):
    _message = 'This email already taken'
    code = status.CONFLICT


class InvalidCredentials(BaseProjectException):
    _message = 'Invalid email or password'
    code = status.UNAUTHORIZED


class UserNotFound(BaseProjectException):
    _message = 'User not found'
    code = status.NOT_FOUND
