from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	headline = "HELLO, CONCAC"
	return render_template("ex7.html", headline=headline)

@app.route("/bye")
def bye():
	headline = "BIEN ME MAY DI"
	return render_template("ex7.html", headline=headline)

@app.route("/by")
def index1():
	names = ["ALICE","BOB", "CHARLIE", "DICK"]
	return render_template("ex6.html", names = names)

@app.route("/ex2")
def index2():
	return render_template("experiment2.html")