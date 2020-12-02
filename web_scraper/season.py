from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def url_builder(year):
    builder = ["https://www.basketball-reference.com/leagues/NBA_"]
    builder.append(str(year))
    builder.append('.html')
    url = "".join(builder)
    print(url)
    return url

# #Champion
# def get_champion(year):
#     url = url_builder(year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = soup.find('div',{'id':'info'}).findAll('p')[2].find('a').getText()
#     print(res)
#     return res

# #MVP
# def get_mvp(year):
#     url = url_builder(year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = soup.find('div',{'id':'info'}).findAll('p')[3].find('a').getText()
#     print(res)
#     return res

# #ROY
# def get_roy(year):
#     url = url_builder(year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = soup.find('div',{'id':'info'}).findAll('p')[4].find('a').getText()
#     print(res)
#     return res

# #PPG Leader
# def get_ppg_leader(year):
#     url = url_builder(year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = soup.find('div',{'id':'info'}).findAll('p')[5].find('a').getText()
#     print(res)
#     return res

# #RPG Leader
# def get_rpg_leader(year):
#     url = url_builder(year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = soup.find('div',{'id':'info'}).findAll('p')[6].find('a').getText()
#     print(res)
#     return res

# #APG Leader
# def get_apg_leader(year):
#     url = url_builder(year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = soup.find('div',{'id':'info'}).findAll('p')[7].find('a').getText()
#     print(res)
#     return res

# #WS Leader
# def get_ws_leader(year):
#     url = url_builder(year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = soup.find('div',{'id':'info'}).findAll('p')[8].find('a').getText()
#     print(res)
#     return res




