import requests
from bs4 import BeautifulSoup

for x in range(100):
    url = "https://www.wikihow.com/Special:Randomizer"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    print(soup.find_all('h1'))
