from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()
def getlinks(url):
    html=urlopen("http://en.wikipedia.org"+url)
    bsobj = BeautifulSoup(html, "lxml")
    try:
        print(bsobj.h1.get_text())
        print(bsobj.find(id="mw-content-text").findAll("p")[0])
        print(bsobj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("lack few attribute")
    for link in bsobj.find_all("a",href=re.compile("^(/wiki/)")): #((?!:).)*$
        if 'href' in link.attrs:                # ^代表开始/wiki/ <a href 代表链接)
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print("------\n"+newPage)
                pages.add(newPage)
                getlinks(newPage)
if __name__=="__main__":
    getlinks("")