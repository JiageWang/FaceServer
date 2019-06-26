from sqlalchemy import Column, Integer, BLOB
from . import db


class Embedding(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    staff = db.relationship('Staff', backref=db.backref('embedding'))
    sid = Column(Integer, db.ForeignKey('staff.id'), unique=True, nullable=True)
    emd = Column(BLOB)
