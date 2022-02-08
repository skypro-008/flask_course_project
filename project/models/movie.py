from project.models.base import BaseMixin
from project.setup_db import db


class Director(BaseMixin, db.Model):
    __tablename__ = 'directors'

    name = db.Column(db.String(100), unique=True, nullable=False)
    movies = db.relationship('Movie', back_populates='director', cascade='delete')


class Genre(BaseMixin, db.Model):
    __tablename__ = 'genres'

    name = db.Column(db.String(100), unique=True, nullable=False)
    movies = db.relationship('Movie', back_populates='genre', cascade='delete')


class Movie(BaseMixin, db.Model):
    __tablename__ = 'movies'

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    trailer = db.Column(db.String(255), nullable=True)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    genre = db.relationship('Genre', back_populates='movies')
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False)
    director = db.relationship('Director', back_populates='movies')
