from typing import Dict


class BaseProjectException(Exception):
    message: str = ''

    @classmethod
    def to_dict(cls) -> Dict[str, str]:
        return {'message': cls.message}


class UserAlreadyExists(BaseProjectException):
    message = 'This email already taken'
