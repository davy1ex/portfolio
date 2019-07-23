from flask import render_template, redirect

from app import app
from models import Project, User
from forms import LoginForm

from flask_login import current_user, login_user


@app.errorhandler(404)
def not_found(e):
    return render_template("not_found.html"), 404


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()

        if user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect("/admin")

    return render_template("login.html", form=form)    


@app.route("/about_me")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)
