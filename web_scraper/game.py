from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def url_builder(year,month,day,home_team):
    builder = ["https://www.basketball-reference.com/boxscores/"]
    builder.append(str(year))
    if month < 10:
        builder.append('0')
    builder.append(str(month))
    if day < 10:
        builder.append('0')
    builder.append(str(day))
    builder.append('0')
    builder.append(home_team)
    builder.append('.html')
    url = "".join(builder)
    return url



        


def get_away_team(year,month,day,home_team,soup = None):
    if soup is None:
        url = url_builder(year,month,day,home_team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    res = soup.find("div",{"class": "scorebox"}).find("div",{"itemprop":"performer"}).find("strong").getText().strip('\n\t')
    # print(res)
    return res


def get_game_location(year,month,day,home_team,soup = None):
    if soup is None:
        url = url_builder(year,month,day,home_team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    res = soup.find("div",{"class": "scorebox_meta"}).findAll("div")[1].getText().strip('\n\t')
    return res


def get_table(year,month,day,home_team,t,soup = None):
    if soup is None:
        url = url_builder(year,month,day,home_team)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    table = soup.findAll("table")[t]
    headers = [th.getText() for th in table.find('thead').findAll('tr')[1].findAll('th')]
    headers[0] = "Player"
    headers[-1] = 'Plus-Minus'
    rows = table.find('tbody').findAll('tr') + table.find('tfoot').findAll('tr')
    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                    for i in range(len(rows)) if i != 5]

    res = pd.DataFrame(data, columns = headers).to_dict(orient='index')
    # print(res)
    return res

def get_game_table(year,month,day,home_team,team='HOME',stats='BASIC',time="G",soup=None):
    if team == 'HOME':
        i = 0
    elif team == 'AWAY':
        i = 8
    if stats == 'ADVANCED':
        return get_table(year,month,day,home_team,i+7,soup)
    elif stats == 'BASIC':
        if time == 'G':
            return get_table(year,month,day,home_team,i,soup)
        elif time == "Q1":
            return get_table(year,month,day,home_team,i+1,soup)
        elif time == "Q2":
            return get_table(year,month,day,home_team,i+2,soup)
        elif time == "H1":
            return get_table(year,month,day,home_team,i+3,soup)
        elif time == "Q3":
            return get_table(year,month,day,home_team,i+4,soup)
        elif time == "Q4":
            return get_table(year,month,day,home_team,i+5,soup)
        elif time == "H2":
            return get_table(year,month,day,home_team,i+6,soup)

    




def get_game(year,month,day,home_team):
    url = url_builder(year,month,day,home_team)
    # print(url)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    res = {}
    res["away_team"] = get_away_team(year,month,day,home_team,soup)
    res["game_location"] = get_game_location(year,month,day,home_team,soup)

    teams = ['HOME','HOME','HOME','HOME','HOME','HOME','HOME','HOME','AWAY','AWAY','AWAY','AWAY','AWAY','AWAY','AWAY','AWAY']
    boxes = ['BASIC','BASIC','BASIC','BASIC','BASIC','BASIC','BASIC','ADVANCED','BASIC','BASIC','BASIC','BASIC','BASIC','BASIC','BASIC','ADVANCED']
    times = ['G','Q1','Q2','H1','Q3','Q4','H2','','G','Q1','Q2','H1','Q3','Q4','H2','']
    for i in range(16):
        key = ['boxscore']
        key.append(teams[i])
        key.append(boxes[i])
        if times[i]:
            key.append(times[i])
        key = '_'.join(key).lower()
        table = get_game_table(year,month,day,home_team,teams[i],boxes[i],times[i],soup)
        res[key] = table
    # print(res)
    return res
