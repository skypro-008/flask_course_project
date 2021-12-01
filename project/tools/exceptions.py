from http import HTTPStatus as status
from typing import Dict


class BaseProjectException(Exception):
    _message: str = 'Something went wrong'
    code: int = status.INTERNAL_SERVER_ERROR

    @classmethod
    @property
    def message(cls) -> Dict[str, str]:
        return {'message': cls._message}


class ItemNotFoundException(BaseProjectException):
    code = status.NOT_FOUND


class UserAlreadyExists(BaseProjectException):
    _message = 'This email already taken'
    code = status.CONFLICT


class InvalidCredentials(BaseProjectException):
    _message = 'Invalid email or password'
    code = status.UNAUTHORIZED


class UserNotFoundException(ItemNotFoundException):
    _message = 'User not found'


class PasswordsMismatch(BaseProjectException):
    _message = 'Passwords mismatch'
    code = status.BAD_REQUEST


class GenreNotFoundException(ItemNotFoundException):
    _message = 'Genre not found'


class MovieNotFoundException(ItemNotFoundException):
    _message = 'Movie not found'


class DirectorNotFoundException(ItemNotFoundException):
    _message = 'Director not found'
