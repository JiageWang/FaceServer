from flask import Flask
from flask_cors import CORS
from .models import db, Staff, Record


def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object('app.config')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    CORS(app, supports_credentials=True)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)





