import cv2
import json
import numpy as np
from werkzeug.datastructures import MultiDict
from flask import request, jsonify, make_response
from app.forms import RegisterForm
from app.libs import face_model
from app.models import Staff, db, Embedding
from . import web


@web.route('/register', methods=['POST'])
def register():
    form = RegisterForm(MultiDict({**request.form.to_dict(), **request.files.to_dict()}))
    if form.validate():
        staff = Staff(number=form.number.data,
                      name=form.name.data,
                      branch=form.branch.data,
                      duty=form.duty.data)

        img = cv2.imdecode(np.fromstring(form.img.data.read(), np.uint8), cv2.IMREAD_COLOR)
        emd = bytes(json.dumps(face_model.get_embedding(img).tolist()), encoding='utf-8')
        try:
            db.session.add(staff)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return make_response(jsonify({'msg': '写入数据库失败: add staff'}), 400)
        sid = Staff.query.filter_by(number=form.number.data).first().id
        embedding = Embedding(sid=sid, emd=emd)
        try:
            db.session.add(embedding)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return make_response(jsonify({'msg': '写入数据库失败: add embedding'}), 400)
        face_model.update_facebank()
        return make_response(jsonify({'msg': '注册成功'}))
    else:
        return make_response(jsonify({'msg': '参数验证失败'}), 400)
