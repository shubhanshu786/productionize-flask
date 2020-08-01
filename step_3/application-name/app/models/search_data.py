from app import db
from sqlalchemy.dialects.sqlite import INTEGER, VARCHAR, JSON
from sqlalchemy import Column
import json
from app.utils.db_utils import AlchemyEncoder


class OldData(db.Model):
    __tablename__ = 'old_data'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    text = Column(VARCHAR, unique=False, nullable=False)
    results = Column(JSON, nullable=True)

    # How data will be represented. Serializer
    def __repr__(self):
        return json.dumps(self, cls=AlchemyEncoder)
