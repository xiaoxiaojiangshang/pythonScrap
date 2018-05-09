from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read(), "lxml")
        title=bsobj.h1
    except AttributeError as e:
        return None
    return title

title=get_title("http://www.pythonscraping.com/pages/page1.html")
if title==None:
    print("No title")
else:
    print(title)


