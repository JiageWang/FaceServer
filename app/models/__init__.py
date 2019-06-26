from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from app.models.staff import Staff
from app.models.record import Record
from app.models.embedding import Embedding
