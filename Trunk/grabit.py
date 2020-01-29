from bs4 import BeautifulSoup
import requests

link = "https://www.geeksforgeeks.org/difference-between-multitasking-multithreading-and-multiprocessing/"

page = requests.get(link)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find_all('article'))

