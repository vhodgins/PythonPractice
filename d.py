import requests
from bs4 import BeautifulSoup

url1 = 'https://www.facebook.com'
url = 'https://www.facebook.com/groups/1990275351235065/'

doc = requests.get(url, auth=('v3hodgins@gmail.com', 'Mar1anne'))

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}


with requests.Session() as s:
    url = 'https://www.facebook.com'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r, 'html.parser')
    print(soup)


#html = open('C:\\Users\\v3hod\\Desktop\\bingtext.txt' 'r')



