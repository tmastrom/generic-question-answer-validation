
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def search_google(query):
    for url in search(query, tld="co.in", num=20, stop=20, pause=2):
        if "wikipedia" in url:
            return url
        else: return None