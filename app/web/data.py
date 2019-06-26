import datetime
from flask import jsonify, request, make_response
from app.forms import RecordSearchForm
from app.models import Staff, Record
from app.view_model import StaffCollection, RecordCollection
from . import web


@web.route('/data/staff')
def staffs_info():
    data = StaffCollection().fill(Staff.query.all()).staffs
    response = make_response(jsonify(data), 200)

    return response


@web.route('/data/record')
def records_info():
    data = RecordCollection().fill(Record.query.all()).records
    response = make_response(jsonify(data), 200)

    return response
