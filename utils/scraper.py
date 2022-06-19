import requests
from bs4 import BeautifulSoup

def wiki_scraper(wikiUrl):

    response = requests.get( 
        url = wikiUrl
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the article body 
    body = soup.find(id="mw-content-text").text
    lines = body.splitlines()

    # read from back of document and cut it at "see also"
    # TODO remove "[edit]" ??
    i = len(lines)
    for line in reversed(lines): 
        if "see also" in line.lower().strip():
            del lines[i-1]
            break
        del lines[i-1]
        i-= 1

    # return list of text lines, remove empty strings
    return list(filter(lambda line: line.strip() != "", lines))

# print(wiki_scraper("https://en.wikipedia.org/wiki/Python_(programming_language)"))