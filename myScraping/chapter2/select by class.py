from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj=BeautifulSoup(html,"lxml")
# namelist=bsobj.find_all("div",{"id":"text"})
namelist=bsobj.find_all(text="the prince")
for name in namelist:
    print(name.get_text(),'\n')  #get_text delete tag like span