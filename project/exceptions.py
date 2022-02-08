from http import HTTPStatus
from typing import Dict


class BaseProjectException(Exception):
    _message: str = 'Something went wrong'
    code: int = HTTPStatus.INTERNAL_SERVER_ERROR

    @classmethod
    @property
    def message(cls) -> Dict[str, str]:
        return {'message': cls._message}


class ItemNotFoundException(BaseProjectException):
    code = HTTPStatus.NOT_FOUND


class UserAlreadyExists(BaseProjectException):
    _message = 'This email already taken'
    code = HTTPStatus.CONFLICT


class InvalidCredentials(BaseProjectException):
    _message = 'Invalid email or password'
    code = HTTPStatus.UNAUTHORIZED


class GenreNotFoundException(ItemNotFoundException):
    _message = 'Genre not found'


class MovieNotFoundException(ItemNotFoundException):
    _message = 'Movie not found'


class DirectorNotFoundException(ItemNotFoundException):
    _message = 'Director not found'


class InvalidOrExpiredRefreshToken(BaseProjectException):
    _message = 'Invalid refresh token or token expired'
    code = HTTPStatus.UNAUTHORIZED


class UpdatePasswordException(BaseProjectException):
    _message = 'Fail to change user password'
    code = HTTPStatus.BAD_REQUEST
