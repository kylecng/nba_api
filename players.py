from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import asyncio

url = "https://www.basketball-reference.com/players/a/abdulka01.html"

html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")
# print(soup.getText())

headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
# print(headers)

rows = soup.findAll('tbody')[0].findAll('tr')
# print(rows)



player_stats = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
            for i in range(len(rows))]
# print(player_stats)

stats = pd.DataFrame(player_stats, columns = headers)
stats.head(10)

##games played
# print(soup.find('div', {'class' : 'stats_pullout'}).findAll('p')[3].getText())

print(soup.getText())
