import configparser

config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

SQLALCHEMY_DATABASE_URI = config.get('db', 'SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = True if int(config.get('db', 'SQLALCHEMY_TRACK_MODIFICATIONS')) else False
HOST = config.get('url', 'HOST')
PORT = int(config.get('url', 'PORT'))
INTERVAL = int(config.get('setting', 'INTERVAL'))
DEBUG = True if int(config.get('setting', 'DEBUG')) else False
CUDA = True if int(config.get('setting', 'CUDA')) else False
