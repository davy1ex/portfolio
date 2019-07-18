from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about_me")
def test():
    return render_template("about.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("not_found.html"), 404


if __name__ == "__main__":
    app.run()