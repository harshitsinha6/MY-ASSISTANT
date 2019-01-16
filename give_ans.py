from bs4 import BeautifulSoup as bs
import urllib

#query = 'dilber'
def finding_url(query):
    from googlesearch import search
    req_url = ''
    for i in search(query, tld = 'co.in', num = 10, stop = 1, pause = 2):
    #print(i)
        if('wiki' in i):
            req_url = i
            print('-->>>',req_url)

    return req_url

def scraping(url):
    src = urllib.request.urlopen(url)
    soup = bs(src, "html.parser")
    #print(soup.body.text)
    return soup.title.text

def find_wiki(query):
    import wikipedia
    info = wikipedia.summary(query, sentences = 2)
    return info
  
"""def main():
    query = 'dilber'
    url = finding_url(query)
    print(finding_url(query))
    text = scraping(url)
    print(text)



#main()
#print(scraping('https://en.wikipedia.org/wiki/catch'))
#print(scraping('https://dictionary.cambridge.org/dictionary/english/catch'))
"""
