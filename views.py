from flask import render_template

from app import app
from models import Project


@app.errorhandler(404)
def not_found(e):
    return render_template("not_found.html"), 404


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about_me")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)



