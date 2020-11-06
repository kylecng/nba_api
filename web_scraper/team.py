from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def url_builder(team):
    builder = ["https://www.basketball-reference.com/teams/"]
    builder.append(team)
    url = "".join(builder)
    print(url)
    return url

#Location
def get_location(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[2].getText()
    s = text.split()
    res = ' '.join(s[1:])
    print(res)
    return res

#Team Names
def get_team_names(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[3].getText()
    s = text.split()
    text = text[15:-1]
    res = dict(enumerate(text.split(', ')))
    print(res)

#Number of Seasons
def get_num_seasons(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[4].getText()
    s = text.split()
    res = int(s[1][:-1])
    print(res)
    return res

#Record
def get_record(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[5].getText()
    s = text.split()
    record = s[1][:-1].split('-')
    res = {"wins": int(record[0]), "losses": int(record[1])}
    print(res)
    return res

#Playoff Appearances
def get_num_playoffs(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[6].getText()
    s = text.split()
    res = int(s[2])
    print(res)
    return res

#Number of Championships
def get_num_champs(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[7].getText()
    s = text.split()
    res = int(s[1])
    print(res)
    return res

#Seasons
def get_seasons(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
    
    rows = soup.findAll('tbody')[0].findAll('tr')
    

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    
    res = pd.DataFrame(data, columns = headers)
    print(res)
    return res