from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, func, Integer

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())
