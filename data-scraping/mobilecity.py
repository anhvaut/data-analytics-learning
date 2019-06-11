from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
def not_relative_uri(href):
    return re.compile('^https://').search(href) is  not  None

url =  'https://mobilecity.vn'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feeds = soup.find_all(
    'div', class_="service-item-left")

df = pd.DataFrame(columns=['title', 'href'])

for feed in new_feeds:
    link = feed.find('a').get('href')
    title = feed.find('a').get('title')
    print('Title: {} - Link: {}'.format(title, link))
    

df.to_csv('mobilecity.csv', sep='\t', encoding='utf-8')
