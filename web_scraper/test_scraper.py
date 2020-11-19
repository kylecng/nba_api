from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/players/j/jamesle01.html#all_adj-shooting"

html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")
print(soup.getText())