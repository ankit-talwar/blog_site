import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = (soup.select('.storylink'))
subtext = soup.select('.subtext')

def sorted_news_by_score(news):
     return sorted(news, key= lambda k:k['votes'], reverse=True)
def create_custom_news(links, subtext):
    news = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))

            if points > 99:
                news.append({'title':title, 'link':href, 'votes':points})
    return sorted_news_by_score(news)
pprint.pprint(create_custom_news(links, subtext))