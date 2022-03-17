from project.setup import db
from project.setup.db.models import Base

favorite = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
)


class User(Base):
    __tablename__ = 'users'

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    surname = db.Column(db.String(50), nullable=True)
    favourite_genre = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=True)
    favorites = db.relationship(
        'Movie',
        secondary=favorite,
        lazy='subquery',
        backref=db.backref('movies', lazy=True),
    )
