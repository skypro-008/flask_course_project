from calendar import timegm
from datetime import datetime, timedelta
from typing import Any, Dict

import jwt
from flask import current_app


class JwtToken:
    def __init__(self, data: Dict[str, Any]):
        self._now = datetime.utcnow()
        self._data = data
        self._access_token_expiration: int = current_app.config['TOKEN_EXPIRE_MINUTES']
        self._refresh_token_expiration: int = current_app.config['TOKEN_EXPIRE_DAYS']

    def _get__token(self, time_delta: timedelta):
        self._data.update({'exp': timegm((self._now + time_delta).timetuple())})
        return jwt.encode(
            self._data, current_app.config['SECRET_KEY'], algorithm='HS256'
        )

    @property
    def access_token(self) -> str:
        return self._get__token(timedelta(minutes=self._access_token_expiration))

    @property
    def refresh_token(self) -> str:
        return self._get__token(timedelta(days=self._refresh_token_expiration))

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])

    def get_tokens(self) -> Dict[str, str]:
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
        }
