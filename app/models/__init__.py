from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def save_commit(self):
        try:
            yield
            self.session.commit()
        except Exception:
            self.session.rollback()


db = SQLAlchemy()

from app.models.staff import Staff
from app.models.record import Record
from app.models.embedding import Embedding
