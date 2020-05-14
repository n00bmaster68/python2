from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline = "HELLO, EVERYONE"
	return render_template("ex7.html", headline = headline)

@app.route("/more")
def more():
	return render_template("more.html")