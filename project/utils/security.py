import base64
import hashlib
import hmac
from typing import Union

from flask import current_app


def generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=password.encode('utf-8'),
        salt=current_app.config['PWD_HASH_SALT'],
        iterations=current_app.config['PWD_HASH_ITERATIONS'],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(generate_password_digest(password)).decode('utf-8')


def compare_passwords(password_hash: Union[str, bytes], password: str):
    return hmac.compare_digest(
        base64.b64decode(password_hash), generate_password_digest(password)
    )
