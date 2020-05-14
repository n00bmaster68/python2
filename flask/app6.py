from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'prettyprinted'
app.config["SESION_PERMANENT"] = False
app.config["SESION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET","POST"])
def index():
	if session.get("notes") is None:
		session["notes"] = []
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)

	return render_template("ex9.html", notes=session["notes"])
