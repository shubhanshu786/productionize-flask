from app import db
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy import Column


class Users(db.Model):
    __tablename__ = 'user' # Optional
    id = Column(INTEGER, autoincrement=True, primary_key=True, unique=True)
    name = Column(VARCHAR(64), unique=True, nullable=False)
    password = Column(VARCHAR(64), nullable=False)