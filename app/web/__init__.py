from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import face, index, data, register
