from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def url_builder(team,soup=None):
    builder = ["https://www.basketball-reference.com/teams/"]
    builder.append(team)
    url = "".join(builder)
    print(url)
    return url

def get_team(team):
    url = url_builder(team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    res = {}
    res['team_location'] = get_team_location(team,soup)
    res['team_names'] = get_team_names(team,soup)
    res['num_seasons'] = get_num_seasons(team,soup)
    res['record'] = get_record(team,soup)
    res['num_playoffs'] = get_num_playoffs(team,soup)
    res['num_champs'] = get_num_champs(team,soup)
    res['seasons_stats'] = get_seasons_stats(team,soup)

#Location
def get_team_location(team,soup=None):
    if soup is None:
        url = url_builder(team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[2].getText()
    s = text.split()
    res = ' '.join(s[1:])
    print(res)
    return res

#Team Names
def get_team_names(team,soup=None):
    if soup is None:
        url = url_builder(team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[3].getText()
    s = text.split()
    text = text[15:-1]
    res = dict(enumerate(text.split(', ')))
    print(res)

#Number of Seasons
def get_num_seasons(team,soup=None):
    if soup is None:
        url = url_builder(team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[4].getText()
    s = text.split()
    res = int(s[1][:-1])
    print(res)
    return res

#Record
def get_record(team,soup=None):
    if soup is None:
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
def get_num_playoffs(team,soup=None):
    if soup is None:
        url = url_builder(team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[6].getText()
    s = text.split()
    res = int(s[2])
    print(res)
    return res

#Number of Championships
def get_num_champs(team,soup=None):
    if soup is None:
        url = url_builder(team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div",{"id":"info"}).findAll('p')[7].getText()
    s = text.split()
    res = int(s[1])
    print(res)
    return res

#Seasons
def get_seasons_stats(team,soup=None):
    if soup is None:
        url = url_builder(team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
    
    rows = soup.findAll('tbody')[0].findAll('tr')
    

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    
    res = pd.DataFrame(data, columns = headers).to_dict(orient='index')
    print(res)
    return res