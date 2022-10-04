from select import select
from winsound import Beep
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import urllib.request as urllib2
import lxml
from lxml import etree, html

my_data = []

# url = 'https://www.finn.no/job/fulltime/search.html?published=1&q=biologi&sort=RELEVANCE'
# data = requests.get(url)
# soup = bs(data.text, 'html.parser')

parser = 'lxml'  # or 'lxml' (preferred) or 'html5lib', if installed
resp = urllib2.urlopen("https://www.finn.no/job/fulltime/search.html?published=1&q=biologi&sort=RELEVANCE")
soup = bs(resp, parser, from_encoding=resp.info().get_param('charset'))

articles = soup.find_all('div', class_ = 'ads__unit__content')

# bread = soup.find_all('div', class_ = 'ads__unit__content__keys')

# print(type(articles))
# print(articles)


for a in articles:

    tittel = a.find('a', class_ = 'ads__unit__link')
    beskrivelse = a.find('div', class_ = 'ads__unit__content__keys')
    sted = a.find('div', class_ = 'u-stone')
    bedrift = a.find('div', class_ = 'ads__unit__content__list')
    
    my_data.append({"tittel": tittel.text.strip(), "sted": sted.text.strip(), "bedrift": bedrift.text.strip()})

    if beskrivelse != None: my_data.append({"beskrivelse": beskrivelse.text.strip()})

    # description = a.select('div.ads__unit__content__keys')[0].get_text()
    # if a.has_attr('href'):
    #     link = a.select(['href'])
    # else: 
    #     link = 'no link found'

    # my_data.append({"title": title, "description": description})

# for link in articles.find_all('a'):
#     print(link.get('href'))

# table = articles.find_all('a', href=True)
# print(articles)

# for link in articles.find_all('a', href=True):
#     print(link.get('href'))





pprint(my_data)
