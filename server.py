from flask import Flask, render_template, request#, session
# from flask.ext.session import Session

app = Flask(__name__)
# SESSION_TYPE = 'redis'
# app.config.from_object(__name__)
# Session(app)

@app.route("/")
def question():
    return render_template('question.html')

@app.route("/answer", methods = ['POST', 'GET'])
def answer():
    if request.method == 'POST':
        question = request.form.get('question')
        # pass the question entered by the user 
        # session['my_question'] = question
        return render_template('answer.html', question = question)

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        answer = request.form.get('answer')
        question = "Who am I?"
        percent = '99'
        return render_template('result.html', question = question, answer = answer, percent = percent)

