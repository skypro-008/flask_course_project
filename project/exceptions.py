from typing import Dict
from http import HTTPStatus as status


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
