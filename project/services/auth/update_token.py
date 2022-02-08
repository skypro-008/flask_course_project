from typing import Dict

from jwt import PyJWTError

from project.exceptions import InvalidOrExpiredRefreshToken
from project.services import BaseService
from project.utils.jwt_token import JwtToken


class UpdateTokenService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jwt_class = JwtToken

    def execute(self, refresh_token: str) -> Dict[str, str]:
        try:
            return self.jwt_class(
                self.jwt_class.decode_token(refresh_token)
            ).get_tokens()
        except PyJWTError:
            raise InvalidOrExpiredRefreshToken
