import threading
import requests
from bs4 import BeautifulSoup


urls=[
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1,50+1)
]

list_num=[f"{i}" for i in range(1,10)]


def craw(url):
    r=requests.get(url)
    return r.text


def parse(html):
    soup=BeautifulSoup(html,"html.parser")
    links=soup.find_all("a","post-item-title")
    return [(i["href"],i.getText()) for i in links]

def getnum(n):
    for i in n:
       yield i

def collect_num(s):
    return int(s)+1



