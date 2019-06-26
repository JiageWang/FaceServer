from sqlalchemy import Column, Integer, TIMESTAMP
from . import db


class Record(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    staff = db.relationship('Staff', backref=db.backref('record'))
    sid = Column(Integer, db.ForeignKey('staff.id'))
    device = Column(Integer, nullable=False)
    time = Column(TIMESTAMP)

