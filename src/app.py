from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home(name="Guest User"):
    return f"<h1> Hello {name} in Flask </h1>"


@app.route("/json")
def json():
    return jsonify({"key1": "value1", "key2": [1, 2, 3, 4, 5]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
