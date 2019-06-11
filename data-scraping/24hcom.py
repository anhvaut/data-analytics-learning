from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import re

url =  'https://www.24h.com.vn'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feeds = soup.find_all(
    'header', class_="nwsTit titbxdoitrangchu")

df = pd.DataFrame(columns=['title', 'href'])

for feed in new_feeds:
    title = feed.find('a').get('title')
    link = feed.find('a').get('href')
    print('Title: {} - Link: {}'.format(title, link))
    print('\n')
    df = df.append({'title':title, 'href':link}, ignore_index=True)

df.to_csv('24h.csv', sep='\t', encoding='utf-8')
    
