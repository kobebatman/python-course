import requests
import email_sender
from bs4 import BeautifulSoup

def do_web_scraping():
    response = requests.get('https://news.ycombinator.com/news')
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    links = soup.select('.storylink')
    points = soup.select('.score')

    def do_scraping(links, points):
        data = []
        for index, link in enumerate(links):
            item = {
                'link': link.get('href'),
                'title': link.string,
                'points': int(points[index].string.replace(' points', ''))
            }
            data.append(item)
        return data
    return do_scraping(links, points)