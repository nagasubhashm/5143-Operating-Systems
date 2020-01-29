#!/usr/local/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

def get_questions(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    to_remove = soup.find_all("div",class_="mobile-incontent-ads") 
    for element in to_remove:
        element.extract()
    #results = tags.find('div', id='content')
    # article = results.find('article')
    questions = soup.find('div',class_='entry-content')
    print(questions.prettify())
    q = questions.find('p')
    print(q)
    


if __name__=='__main__':
    with open("op_sys_topics.html") as f:
        data = f.read()

    
    soup = BeautifulSoup(data, "html.parser")
  
    results = soup.find_all('a')
    for link in results:
        # print(link['href'])
        # print(link.text)
        get_questions(link['href'])
        sys.exit()
