import requests
from bs4 import BeautifulSoup
import time


print("Find the Orbital Period of Which planet?")
x = str(input())
t1 = time.time()
url = 'https://en.wikipedia.org/wiki/' + x + '_(planet)'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser').prettify()
location = soup.find('Orbital period', 0, len(soup))
words = ''
words2 = ''

for c in soup[location:location+500]:
    words = words + c

newlist = words.split()

p = 0
g = 0

for c in newlist:
    if '.' in c and p == 0:
        words2 = words2 + c
        p = 1
    if 'd' in c and g == 0 and p == 1 :
        words2 = words2 + ' days'
        g = 1
    if 'year' in c and g == 0 and p == 1 :
        words2 = words2 + ' years'
        g = 1

print(words2)
print('This took ' + str(round(100*(time.time() - t1))/100) + ' seconds')

