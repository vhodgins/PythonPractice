from __future__ import print_function

import requests
from bs4 import BeautifulSoup


def wikihow_fetch():
    url = "https://www.wikihow.com/Special:Randomizer"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    d = str(soup.select('h1 a'))
    collect_letters = False
    title = ''
    collect_link = -1
    link = ''
    for x in d:
        if x == '<':
            collect_letters = False

        if collect_letters == True:
            if x != ']':
                title += x

        if collect_link == 1:

            if x != '"':
                link += x

        if x == '>':
            collect_letters = True
        if x == '"':
            collect_link *= -1
    return title, link

def warframe_fetch():
    url = "https://warframe.fandom.com/wiki/Special:Random"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    d = str(soup.select('h1 a'))
    collect_letters = False
    title = ''
    collect_link = -1
    link = ''
    for x in d:
        if x == '<':
            collect_letters = False

        if collect_letters == True:
            if x != ']':
                title += x

        if collect_link == 1:

            if x != '"':
                link += x

        if x == '>':
            collect_letters = True
        if x == '"':
            collect_link *= -1
    return title, link
