from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import face
from app.web import index
from app.web import data
