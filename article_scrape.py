"""
    Homework 3.01: article_scrape.py
    Author: Em Longan
    Last modified: 02/03/2025
"""
from bs4 import BeautifulSoup
import requests

frogs = 'https://apnews.com/article/london-zoo-darwins-frogs-chile-endangered-eeaa384fdbfdbd89969514c14dca53cb'

response = requests.get(frogs)
soup = BeautifulSoup(response.text, 'html.parser')

# <meta property="og:title" content="Scientists hope these tiny froglets can save their species">
title_tag = soup.find('meta', attrs={'property': 'og:title'})

#<meta property="article:author" content="https://apnews.com/author/sylvia-hui">
author_tag = soup.find('meta', attrs={'property': 'article:author'})

# <meta property="article:published_time" content="2025-02-03T13:38:31">
pub_tag = soup.find('meta', attrs={'property': 'article:published_time'})
date = pub_tag.get('content')

print(f'Title: {title_tag.get('content')}')
print(f'Byline: {author_tag.get('content')}')
print(f'Date: {date[0:10]}')

ptags = soup.find_all('div', attrs={'class': 'RichTextStoryBody RichTextBody'})
for tag in ptags:
    print(tag.text)