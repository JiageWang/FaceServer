from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from . import db


class Record(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    name = Column(String(30), nullable=False)
    time = Column(DateTime, nullable=False)
    device = Column(Integer, nullable=False)

