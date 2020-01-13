import requests
from bs4 import BeautifulSoup
import random
import re

def synonym(word):
    url = "https://www.synonyms.com/synonym/" + word
    record = 1
    synonymlist = []

    r = requests.get(url)
    r_html = r.text
    page = BeautifulSoup(r_html, "html.parser")
    synonyms = page.select("p.syns a")

    for i in synonyms:
        word1 = ''
        for x in i:
             word1 += x
        synonymlist.append(word1)



    return random.choice(synonymlist)


def synonymsentence(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.split()
    newsentence = []
    for x in sentence:
        newsentence.append(synonym(x)+ ' ')

    return ''.join(newsentence)


