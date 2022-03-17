from typing import Dict

from jwt import PyJWTError
from marshmallow import ValidationError
from marshmallow.fields import Email, Integer
from marshmallow.schema import BaseSchema

from project.dao import GenreDAO, UserDAO
from project.errors import AuthenticationError, BadRequestError
from project.models import User
from project.services.base import BaseService
from project.utils.jwt_token import JwtToken
from project.utils.security import compare_passwords, generate_password_hash


class UserSchema(BaseSchema):
    id = Integer(required=True)
    email = Email(required=True)


class AuthService(BaseService):
    def __init__(self, db_session) -> None:
        super().__init__(db_session)
        self.dao = UserDAO(db_session)
        self.schema = UserSchema()

    def register_user(self, email: str, password: str) -> None:
        self.dao.create(email=email, password=generate_password_hash(password))

    def check_user_credentials(self, email: str, password: str) -> Dict[str, str]:
        if not (user := self.dao.get_user_by_email(email)):
            raise AuthenticationError

        if not compare_passwords(user.password, password):
            raise AuthenticationError

        return JwtToken(self.schema.dump(user)).get_tokens()

    def get_user_profile(self, user_id: int) -> User:
        return self.dao.get_by_id(pk=user_id)

    def update_tokens(self, refresh_token: str) -> Dict[str, str]:
        try:
            data = self.schema.load(
                data=JwtToken.decode_token(refresh_token),
                unknown='EXCLUDE'
            )
        except PyJWTError:
            raise AuthenticationError('Expired refresh token')
        except ValidationError:
            raise AuthenticationError('Invalid refresh token')
        else:
            return JwtToken(data).get_tokens()

    def update_user_profile(self, user_id: int, **kwargs) -> User:

        # Проверяем, что пользователь существует
        self.dao.get_by_id(pk=user_id)

        data = {}
        if favourite_genre_id := kwargs.get('favourite_genre'):
            # Проверяем существование жанра
            data['favourite_genre'] = GenreDAO(self._db_session).get_by_id(favourite_genre_id).id

        if name := kwargs.get('name'):
            data['name'] = name

        if surname := kwargs.get('surname'):
            data['surname'] = surname

        return self.dao.update(user_id=user_id, **data)

    def update_user_password(self, user_id: int, old_password: str, new_password: str) -> None:
        if user := self.dao.get_by_id(pk=user_id):
            if compare_passwords(user.password, old_password):
                self.dao.update_password(
                    user_id=user_id,
                    password=generate_password_hash(new_password)
                )
                return None

        raise BadRequestError('Fail to change user password')
