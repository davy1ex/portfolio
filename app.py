from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_admin import Admin

from flask_admin import form
import random
import os
from flask_admin.contrib.sqla import ModelView

from flask_login import LoginManager, current_user

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

from models import Project
admin = Admin(app, base_template='custom_admin.html')




def prefix_name(obj, file_data):
    parts = os.path.splitext(file_data.filename)
    return secure_filename("file-%s%s" % parts)


class ProjectModelView(ModelView):

    form_extra_fields = {
        "photo": form.FileUploadField("photo", base_path="static/img")
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                hash = random.getrandbits(64)
                ext =storage_file.filename.split(".")[-1]
                path = "%s.%s" % (hash, ext)

                print(path)

                storage_file_save(os.path.join(app.config["STORAGE"], path))
                _form.photo.data = path

                del _form.file
        except Exception as ex:
            pass

        return _form

    def edit_form(self, obj=None):
        return self._change_path_data(super(ProjectModelView, self).edit_form(obj))
    
    def create_form(self, obj=None):
        return self._change_path_data(super(ProjectModelView, self).create_form(obj))
    
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.login == "root"
        else:
            pass

        


admin.add_view(ProjectModelView(Project, db.session))
