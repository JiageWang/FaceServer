from flask_sqlalchemy import SQLAlchemy


# class SQLAlchemy(_SQLAlchemy):
#     def safe_commit(self):
#         try:
#             yield
#             self.session.commit()
#         except Exception as e:
#             self.session.rollback()
#             raise e


db = SQLAlchemy()
from app.models.staff import Staff
from app.models.record import Record
