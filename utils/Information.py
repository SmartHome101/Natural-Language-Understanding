import requests
import wikipedia
from bs4 import BeautifulSoup
import wolframalpha




# To get information such as (Topic Definition , Topic Summary)
if result['Intent'] == 'Info_Request' and 'topic' in result['Entities']:
    searchtext = result['Entities']['topic']
    url = 'https://www.dictionary.com/browse/'
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    })
    wikistr = wikipedia.summary(searchtext, sentences=3)
    index = wikistr.find(searchtext)
    if (index != -1):
        wikidef = wikipedia.summary(searchtext, sentences=3)
        print(wikidef)
    else:
        req = requests.get(url + searchtext, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        mydivs = soup.findAll("div", {"value": "1"})[0]

        for tags in mydivs:
            meaning = tags.text
            
        print(meaning)
        
        
# To get answers for the questions
def info(text):
    
    # Taking input from user
    question = text

    #id obtained by the above steps
    Id = 'GQLHYV-3UTAKGPWQT'

    # Instance of wolframalpha client class
    client = wolframalpha.Client(Id)

    # Stores the response from wolframalpha
    res = client.query(question)

    # Includes only text from the response
    answer = next(res.results).text

    return answer