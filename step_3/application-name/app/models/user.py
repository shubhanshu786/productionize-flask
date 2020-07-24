from app import db
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy import Column
import json
from app.utils.db_utils import AlchemyEncoder


class Users(db.Model):
    __tablename__ = 'user' # Optional
    id = Column(INTEGER, autoincrement=True, primary_key=True, unique=True)
    name = Column(VARCHAR(64), unique=True, nullable=False)
    password = Column(VARCHAR(64), nullable=False)

    # How data will be represented. Serializer
    def __repr__(self):
        return json.dumps(self, cls=AlchemyEncoder)