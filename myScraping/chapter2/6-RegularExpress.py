from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj=BeautifulSoup(html,"lxml")

images=bsobj.find_all("img",{"src":re.compile("\.\.\/img\/gifts\/img.\.jpg")})
for image in images:
    print(image)
    print (type(image))