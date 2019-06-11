from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd

def  not_relative_uri(href):
    return re.compile('^https://').search(href) is  not  None

url = 'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

df = pd.DataFrame(columns=['title', 'href'])

new_feeds = soup.find(
    'section', class_='featured container clearfix').find_all(
        'a', class_='', href=not_relative_uri)
for feed in new_feeds:
    title = feed.get('title')
    link = feed.get('href')
    print('Title: {} - Link: {}'.format(title, link))

df.to_csv('vnexpress.csv', sep='\t', encoding='utf-8')
