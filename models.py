from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    photo = db.Column(db.String(128))
    description = db.Column(db.String(512))
    git_link = db.Column(db.String(128))

    def __repr__(self):
        return "{1}. {2}".format(self.id, self.title)
