from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("ex8.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
	if request.method == "GET":
		return "PLS SUBMIT YOUR INFOR"
	else:
		name = request.form.get("name")
		dob = request.form.get("date of birth")
		gender = request.form.get("gender")
		pw = request.form.get("password")
		return render_template("helloKT.html", name=name, dob=dob, gender=gender, pw=pw)