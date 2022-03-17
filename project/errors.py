from http import HTTPStatus


class BaseProjectException(Exception):
    message: str = 'Oops'
    code: int = 500

    def __init__(self, message: str = '', *, code: int = 500):
        super().__init__()
        if message:
            self.message = message
        self.code = code


class NotFoundErro(BaseProjectException):
    def __init__(self, message: str = 'Not Found'):
        super().__init__(message, code=HTTPStatus.NOT_FOUND)


class ConflictError(BaseProjectException):
    def __init__(self, message: str = 'Record already exists'):
        super().__init__(message, code=HTTPStatus.CONFLICT)


class AuthenticationError(BaseProjectException):
    def __init__(self, message: str = 'Invalid credentials'):
        super().__init__(message, code=HTTPStatus.UNAUTHORIZED)


class BadRequestError(BaseProjectException):
    def __init__(self, message: str = 'Bad request'):
        super().__init__(message, code=HTTPStatus.BAD_REQUEST)
