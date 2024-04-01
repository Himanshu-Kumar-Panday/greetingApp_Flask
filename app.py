from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "fbdhbfjhs"

@app.route("/")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST","GET"])        #interacting with the server so need to mention the methods
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    return render_template("index.html")