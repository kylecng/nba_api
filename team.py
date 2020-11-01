from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/teams/ATL/"

html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")
# print(soup.getText())

#Location
def get_location():
    text = soup.find("div",{"id":"info"}).findAll('p')[2].getText()
    s = text.split()
    res = ' '.join(s[1:])
    print(res)
    return res
get_location()

#Team Names
def get_team_names():
    text = soup.find("div",{"id":"info"}).findAll('p')[3].getText()
    s = text.split()
    text = text[15:-1]
    res = text.split(', ')
    print(res)
get_team_names()
#Number of Seasons
def get_num_seasons():
    text = soup.find("div",{"id":"info"}).findAll('p')[4].getText()
    s = text.split()
    res = int(s[1][:-1])
    print(res)
    return res
get_num_seasons()

#Record
def get_record():
    text = soup.find("div",{"id":"info"}).findAll('p')[5].getText()
    s = text.split()
    record = s[1][:-1].split('-')
    res = {"wins": int(record[0]), "losses": int(record[1])}
    print(res)
get_record()

#Playoff Appearances
def get_num_playoffs():
    text = soup.find("div",{"id":"info"}).findAll('p')[6].getText()
    s = text.split()
    res = int(s[2])
    print(res)
get_num_playoffs()
#Number of Championships

def get_num_champs():
    text = soup.find("div",{"id":"info"}).findAll('p')[7].getText()
    s = text.split()
    res = int(s[1])
    print(res)
    return res
get_num_champs()

#Seasons
def get_seasons():
    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
    

    rows = soup.findAll('tbody')[0].findAll('tr')
    

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    

    stats = pd.DataFrame(data, columns = headers)
    
    print(stats)
get_seasons()