from .auth import auth_ns
from .director import directors_ns
from .favorites import favorites_ns
from .genre import genres_ns
from .movie import movies_ns
from .user import user_ns

__all__ = [
    'auth_ns',
    'directors_ns',
    'favorites_ns',
    'genres_ns',
    'movies_ns',
    'user_ns',
]
