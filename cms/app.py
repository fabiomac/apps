#--* coding: utf-8 *--#
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
	return "Hello World!! <strong> I'm learning Flask </strong>", 200

@app.route("/<name>")
def index(name):
	if name.lower() == "fabio":
		return "Olá {}".format(name), 200
	else:
		return "Not Found!!!", 404
	


app.run(debug=True)