from google import search_google
from scraper import wiki_scraper


question = input("Your question: ")

wikiUrl = search_google(question)

print(wikiUrl)

corpus = wiki_scraper(wikiUrl)
