import os

from flask import Flask, render_template, request, session

from utils.google import search_google
from utils.scraper import wiki_scraper
from utils.nlp import semantic_transform, checkAnswer

app = Flask(__name__)
# Details on the Secret Key: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.
# https://testdriven.io/blog/flask-sessions/
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/", methods = ['GET', 'POST'])
def question():
    return render_template('question.html')

@app.route("/result", methods = ['POST', 'GET'])
def answer():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')
        
        session['question'] = question
        session['answer'] = answer

        # search google for a wiki page on the question topic 
        # TODO: error handling 
        wikiUrl = search_google(question)
        
        # Scrape text from wiki page and return filtered text
        corpus = wiki_scraper(wikiUrl)

        # format the corpus for nlp training
        dictionary, lsi, index = semantic_transform(corpus)

        # check the answer against the semantic vectorization and determine if correct
        percent = checkAnswer(dictionary, lsi, index, answer)

        return render_template('result.html', percent = percent)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))