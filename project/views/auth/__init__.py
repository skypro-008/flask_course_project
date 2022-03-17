from .auth import api as auth_ns
from .user import api as user_ns

__all__ = [
    'auth_ns',
    'user_ns',
]
