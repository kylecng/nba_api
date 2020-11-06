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



def get_away_team(year,month,day,home_team):
    url = url_builder(year,month,day,home_team)
    print(url)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    res = soup.find("div",{"class": "scorebox"}).find("div",{"itemprop":"performer"}).find("strong").getText().strip('\n\t')
    print(res)
    return res


def get_location(year,month,day,home_team):
    url = url_builder(year,month,day,home_team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    res = soup.find("div",{"class": "scorebox_meta"}).findAll("div")[1].getText().strip('\n\t')
    return res


def get_table(year,month,day,home_team,t):
    url = url_builder(year,month,day,home_team)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    table = soup.findAll("table")[t]
    headers = [th.getText() for th in table.find('thead').findAll('tr')[1].findAll('th')]
    headers[0] = "Player"
    rows = table.find('tbody').findAll('tr') + table.find('tfoot').findAll('tr')
    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                    for i in range(len(rows)) if i != 5]

    res = pd.DataFrame(data, columns = headers)
    res = res.to_dict()
    print(res)
    return res

def get_game_table(year,month,day,home_team,team='HOME',stats='BASIC',time="G"):
    if team == 'HOME':
        i = 0
    elif team == 'AWAY':
        i = 8
    if stats == 'ADVANCED':
        return get_table(year,month,day,home_team,i+7)
    elif stats == 'BASIC':
        if time == 'G':
            return get_table(year,month,day,home_team,i)
        elif time == "Q1":
            return get_table(year,month,day,home_team,i+1)
        elif time == "Q2":
            return get_table(year,month,day,home_team,i+2)
        elif time == "H1":
            return get_table(year,month,day,home_team,i+3)
        elif time == "Q3":
            return get_table(year,month,day,home_team,i+4)
        elif time == "Q4":
            return get_table(year,month,day,home_team,i+5)
        elif time == "H2":
            return get_table(year,month,day,home_team,i+6)

    




