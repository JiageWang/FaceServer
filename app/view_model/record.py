import datetime
from flask import current_app
from sqlalchemy import and_
from app import create_app
from app.models import db
from app.models.record import Record


class RecordViewModel:
    def __init__(self):
        self.records = []
        self.num = 0

    @staticmethod
    def __record2dict(record):
        record_dict = {
            'id': record.id,
            'number': record.number,
            'name': record.name,
            'time': record.time,
            'device': record.device
        }
        return record_dict

    def query(self, **condition):
        self.records = [self.__record2dict(record) for record in Record.query.filter_by(**condition).all()]
        self.num = len(self.records)
        return self

    def query_time_device(self, time, device):
        start, end = self.convert_datetime(time)
        result = Record.query.filter(and_(
            Record.time.between(start, end),
            Record.device == device)
        ).all()
        self.records = [self.__record2dict(record) for record in result]
        self.num = len(self.records)
        return self

    def add(self, staff, device):
        record = self.query(name=staff['name'], device=device).last
        now = datetime.datetime.now()
        if record and self.valid_interval(now, record['time']):
            try:
                record = Record(name=staff['name'],
                                number=staff['number'],
                                time=datetime.datetime.now(),
                                device=device)
                db.session.add(record)
                db.session.commit()
                return True
            except Exception as e:
                print('添加数据失败', e)
        return False

    @property
    def last(self):
        return self.records[-1] if self.num > 0 else None

    @staticmethod
    def valid_interval(time1, time2):
        diff = (time1 - time2).seconds
        if diff > current_app.config['INTERVAL']:
            return True
        else:
            return False

    @staticmethod
    def convert_datetime(time):
        time1, time2 = time.split('_')
        start = datetime.datetime(int(time1[:4]), int(time1[4:6]), int(time1[6:]))
        end = datetime.datetime(int(time2[:4]), int(time2[4:6]), int(time2[6:]))
        return start, end


if __name__ == "__main__":
    with create_app().app_context():
        rvm = RecordViewModel()
        firstDay = datetime.datetime(2019, 6, 16, 14, 19, 2)
        lastDay = datetime.datetime(2019, 6, 16, 14, 19, 4)
        print(rvm.query_time_device(Record.time.between(firstDay, lastDay)))
