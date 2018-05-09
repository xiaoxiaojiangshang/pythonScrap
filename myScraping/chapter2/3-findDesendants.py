from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj=BeautifulSoup(html,"lxml")
for child in bsobj.find("table",{"id":"giftList"}).children:
    print(child)

print("different\n")

for siblings in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(siblings)

print("duandiandsajd;l")
print(bsobj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())