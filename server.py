from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def question():
    return render_template('question.html')

@app.route("/answer")
def answer():
    return render_template('answer.html')