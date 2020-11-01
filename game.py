from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/boxscores/202002070BOS.html"

html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")
print(soup.getText())


s = soup.find("div",{"class": "scorebox"}).find("div",{"itemprop":"performer"}).find("strong").getText()
s = soup.find("div",{"class": "scorebox"}).findAll("div",{"itemprop":"performer"})[1].find("strong").getText()
s = soup.find("div",{"class": "scorebox_meta"}).findAll("div")[0].getText()
s = soup.find("div",{"class": "scorebox_meta"}).findAll("div")[1].getText()
print(s)