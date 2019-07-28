from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from app import login

from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    photo = db.Column(db.String(128))
    description = db.Column(db.String(512))
    git_link = db.Column(db.String(128))

    def __repr__(self):
        return "{1}. {2}".format(self.id, self.title)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
