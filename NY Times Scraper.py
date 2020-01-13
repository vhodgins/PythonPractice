import requests
from bs4 import BeautifulSoup

headlines = ''
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')
for headline in soup.find_all('h2'):
    if headline.text == "Listen to ‘The Daily’" or headline.text == "Listen to ‘The Argument’" or headline.text == "Site Index" or headline.text == "Site Information Navigation":
        pass
    else:
        print(headline.text)


