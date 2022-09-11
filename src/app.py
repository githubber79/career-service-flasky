from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Hello world in Flask </h1>"


if "__name__" == "__main__":
    app.run()
