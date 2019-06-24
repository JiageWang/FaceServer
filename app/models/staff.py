from sqlalchemy import Column, Integer, String
from . import db


class Staff(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, unique=True)
    name = Column(String(30), nullable=False)
    branch = Column(String(30))
    duty = Column(String(30))
