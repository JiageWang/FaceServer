import cv2
import numpy as np
from datetime import datetime
from werkzeug.datastructures import MultiDict

from flask import request, jsonify, current_app
from app.models import Staff, Record, db
from app.forms import FaceForm
from app.view_model import StaffViewModel
from app.libs import face_model
from . import web


@web.route('/face', methods=['POST'])
def face():
    form = FaceForm(MultiDict({**request.form.to_dict(), **request.files.to_dict()}))
    if form.validate():
        # 获取图片
        img = cv2.imdecode(np.fromstring(form.img.data.read(), np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            return jsonify({'msg': '上传图片出错'})
        sid = face_model.compare(img)
        if sid is None:
            return jsonify({'msg': '未注册'})
        # 获取人员信息
        staff = Staff.query.filter_by(id=sid).first()
        if len(staff.record) == 0 or valid_interval(staff.record[-1]):
            record = Record(sid=sid, device=form.device.data, time=datetime.now())
            with db.save_commit():
                db.session.add(record)
            print('{}，打卡成功'.format(staff.name))
            return jsonify(StaffViewModel(staff).info)
    return jsonify({'msg': '未知错误'})


def valid_interval(record):
    time1 = datetime.now()
    time2 = record.time
    diff = (time1 - time2).seconds
    if diff > current_app.config['INTERVAL']:
        return True
    else:
        return False
