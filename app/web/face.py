import cv2
import datetime
import numpy as np
from flask import request, jsonify
from werkzeug.datastructures import MultiDict
from app.forms import FaceForm
from app.view_model import RecordViewModel, StaffViewModel
from app.libs import face_model
from . import web


@web.route('/face', methods=['POST'])
def face():
    form = FaceForm(MultiDict({**request.form.to_dict(), **request.files.to_dict()}))
    if form.validate():
        # 获取图片
        img = cv2.imdecode(np.fromstring(form.img.data.read(), np.uint8), cv2.IMREAD_COLOR)
        name = face_model.infer(img) if img is not None else None
        # 获取人员信息
        staff = StaffViewModel().query(name=name).first
        if staff and RecordViewModel().add(staff, form.device.data):
            # 记录打卡
            print('{}，打卡成功'.format(staff['name']))
            return jsonify(staff)
    return jsonify({'msg': '访问错误'})


if __name__ == "__main__":
    time1 = datetime.datetime.now()
    time2 = datetime.datetime(2019, 6, 18, 8, 27)
