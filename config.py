import os

class Config(object):
    FLASK_APP="app.py"
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(32)
    WTF_CSRF_SECRET_KEY = os.urandom(64)