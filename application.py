from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = "putanginamoangbobomo"


@app.route('/')
def hello_world():
    return 'ew'


@app.route('/grade')
def index():
    flash("what is your name?")
    return render_template("index.html")


@app.route('/get_grades', methods=["POST", "GET"])
def sh_grade():
    response = request.form['name_input']
    flash(f"hi {response} great to see you")
    #flash(str(request.form['name_input']))
    return render_template("index.html")
