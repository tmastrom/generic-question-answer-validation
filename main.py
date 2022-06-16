from google import search_google
from scraper import wiki_scraper
from nlp import semantic_transform, checkAnswer

# Get the question input 
question = input("Your question: ")

# search google for a wiki page on the question topic 
# TODO: error handling 
wikiUrl = search_google(question)

# Scrape text from wiki page and save to txt file
r = wiki_scraper(wikiUrl)

# format the corpus for nlp training
dictionary, lsi, index = semantic_transform()

ans = input("Your answer: ")
checkAnswer(dictionary, lsi, index, ans)