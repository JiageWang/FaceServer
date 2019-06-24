import datetime
from flask import jsonify, request, make_response
from app.forms import RecordSearchForm
from app.view_model import StaffViewModel, RecordViewModel
from . import web


@web.route('/data/staff')
def staffs_info():
    data = StaffViewModel().query().staffs
    response = make_response(jsonify(data), 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'

    return response


@web.route('/data/record')
def records_info():
    form = RecordSearchForm(request.args)
    if form.validate():
        data = RecordViewModel().query_time_device(form.time.data, form.device.data).records
        response = make_response(jsonify(data), 200)
    else:
        response =  make_response(jsonify({'msg': '参数验证失败'}), 400)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


