from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getlinks(url):
    html = urlopen("http://en.wikipedia.org"+url)
    bsobj=BeautifulSoup(html,"lxml")
    return bsobj.find("div",{"id":"bodyContent"}).findAll("a",
            href=re.compile("^(/wiki/)((?!:).)*$"))# ^代表开始/wiki/ <a href 代表链接
links=getlinks("/wiki/Kevin_Bacon")
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getlinks(newArticle)

# html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsobj=BeautifulSoup(html,"lxml")
# for link in bsobj.find("div",{"id":"bodyContent"}).findAll("a",
#            href=re.compile("^(/wiki/)((?!:).)*$")):# ^代表开始/wiki/ <a href 代表链接
#     if 'href' in link.attrs:
#         print(link.attrs['href'])