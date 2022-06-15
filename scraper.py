import requests
from bs4 import BeautifulSoup

def wiki_scraper(wikiUrl):

    response = requests.get( 
        url = wikiUrl
    )
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get the article body 
    body = soup.find(id="mw-content-text").text

    with open('body.txt', 'w') as f: 
        f.write(body)
    
    # open text document and read to list of lines
    full_text = open('body.txt', 'r')
    lines = full_text.readlines()
    full_text.close()

    # read from back of document and cut it at "see also"
    # TODO remove "[edit]" ??
    i = len(lines)
    for line in reversed(lines): 
        if "see also" in line.lower().strip():
            del lines[i-1]
            break
        
        del lines[i-1]
        i-= 1

    # read filtered lines to new file and remove empty lines
    new_file = open('filtered.txt', 'w+')
    for line in lines: 
        if line.strip() != "":
            new_file.write(line)
    new_file.close()

    return 'OK'

# wiki_scraper("https://en.wikipedia.org/wiki/Python_(programming_language)")