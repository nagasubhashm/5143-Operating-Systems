#!/usr/local/bin/python3

from bs4 import BeautifulSoup
import re
import urllib2
import requests
from pprint import pprint
import os,sys
import html2markdown

invalid_tags = ['div', 'span']

baseUrl = "https://sites.google.com"

url = "site/mytechnicalcollection/os"
page = requests.get(os.path.join(baseUrl,url))

soup = BeautifulSoup(page.content,features="lxml")
subpages = soup.find('div',{"class":"sites-subpages"}).find_all('span')

del subpages[0]

for page in subpages:
    topicUrl = page.a['href']
    url = "https://sites.google.com"+topicUrl
    subpage = requests.get(url)
    soup = BeautifulSoup(subpage.content,features="lxml")
    
    content = soup.find(attrs={"role": "main"}).table


    for tag in content.findAll(True):
        for attr in [attr for attr in tag.attrs]:
            print(attr)
            if not attr in ['src']:
                del tag[attr]

    for row in content.find_all("tr"):
        for td in row.find_all("td"):
            for tag in invalid_tags: 
                for match in td.findAll(tag):
                    match.replaceWithChildren()
            # for attribute in ["class", "id", "name", "style"]:
            #     del td[attribute]


    print(html2markdown.convert(str(content)))
    sys.exit()
            

    #
    #print(content)


