import cv2
import json
import numpy as np
from werkzeug.datastructures import MultiDict
from flask import request, jsonify
from app.forms import RegisterForm
from app.libs import face_model
from . import web
from app.models import Staff, db, Embedding


@web.route('/register', methods=['POST'])
def register():
    form = RegisterForm(MultiDict({**request.form.to_dict(), **request.files.to_dict()}))
    if form.validate():
        staff = Staff(number=form.number.data,
                      name=form.name.data,
                      branch=form.branch.data,
                      duty=form.duty.data)
        with db.save_commit():
            db.session.add(staff)
        img = cv2.imdecode(np.fromstring(form.img.data.read(), np.uint8), cv2.IMREAD_COLOR)
        emd = bytes(json.dumps(face_model.get_embedding(img).tolist()), encoding='utf-8')
        sid = Staff.query.filter_by(number=form.number.data).first().id
        embedding = Embedding(sid=sid, emd=emd)
        with db.save_commit():
            db.session.add(embedding)
        face_model.update_facebank()
        return jsonify({'msg': '注册成功'})
    else:
        return jsonify(form.errors)

