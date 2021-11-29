from project.models import BaseMixin
from project.tools.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    surname = db.Column(db.String(50), nullable=True)
