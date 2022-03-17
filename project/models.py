from project.setup.db import db, models


class Director(models.Base):
    __tablename__ = 'directors'

    name = db.Column(db.String(100), unique=True, nullable=False)
    movies = db.relationship('Movie', back_populates='director', cascade='delete')


class Genre(models.Base):
    __tablename__ = 'genres'

    name = db.Column(db.String(100), unique=True, nullable=False)
    movies = db.relationship('Movie', back_populates='genre', cascade='delete')


class Movie(models.Base):
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


favorite = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
)


class User(models.Base):
    __tablename__ = 'users'

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    surname = db.Column(db.String(50), nullable=True)
    favourite_genre = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=True)
    favorites = db.relationship(
        Movie,
        secondary=favorite,
        lazy='subquery',
        backref=db.backref('movies', lazy=True),
    )
