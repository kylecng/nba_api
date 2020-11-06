from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re


def url_builder(team,year):
    builder = ["https://www.basketball-reference.com/teams/"]
    builder.append(team)
    builder.append('/')
    builder.append(str(year))
    builder.append('.html')
    url = "".join(builder)
    print(url)
    return url


##record; wins, losses, conference standing
def get_record(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).find("p").getText()
    nums = [int(s) for s in re.split('t|-|,| ',text)if s.isdigit()]
    res = {}
    res["wins"] = nums[0]
    res["losses"] = nums[1]
    res["rank"] = nums[2]
    print(res)
    return res



##Coach
def get_coach(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[2].getText()
    s = text.split()
    res = s[1] + ' ' + s[2]
    print(res)
    return res

##Executive
def get_exec(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[3].getText()
    s = text.split()
    res = s[1] + ' ' + s[2]
    print(res)

##pace
def get_pace(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[5].getText()
    s = text.split()
    res = s[6]
    print(res)
    return res

##Off Rtg
def get_off_rtg(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[6].getText()
    s = text.split()
    res = s[2]
    print(res)
    return res

##Def Rtg
def get_def_rtg(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[6].getText()
    s = text.split()
    res = s[8]
    print(res)
    return res

##Arena
def get_arena(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[9].getText()
    s = text.split()
    res = ""
    i = 1
    print(s)
    while (i < len(s) and s[i] != "Attendance:"):
        res += s[i] + " "
        i += 1
    print(res)
    return res

##Games Table
    ##Game: date, team, home/away, record, result, team record, opponent record
def get_team_games(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    rowText = soup.find("div", {"id":"timeline_results"}).findAll("li",{"class":"result"})
    rowText = [s.getText() for s in rowText]
    headers = ['No.','Date','Home Game','Opponent','Win','Team Score','Opponent Score','Wins','Losses',]
    data = []
    for r in rowText:
        r = r.replace('(',' ').replace(')',' ').strip()
        # print(r)
        s = re.split("-|,| ",r)
        print(s)
        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        row = []
        
        row.append(int(s[0][:-1]))
        row.append(str(months[s[1]] )+ '-' + s[2])
        row.append(not s[3] == '@')

        if row[-1]:
            row.append(s[-4])
            row.append(s[9] == "beat")
            row.append(int(s[-2]))
            row.append(int(s[-1]))
            row.append(int(s[6]))
            row.append(int(s[7]))
            
            
        else:
            row.append(s[4])
            row.append(s[11] == "beat")
            row.append(int(s[-2]))
            row.append(int(s[-1]))
            row.append(int(s[8]))
            row.append(int(s[9]))

        data.append(row)


    res = pd.DataFrame(data, columns = headers).to_dict()
    print(res)
    return res


##Roster Table
def get_roster(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
    rows = soup.find('tbody').findAll('tr')

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]

    res = pd.DataFrame(data, columns = headers).to_dict()
    return res


##Per Game Table
def get_per_game(team,year):
    url = url_builder(team,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    headers = [th.getText() for th in soup.findAll('table')[1].find('tr').findAll('th')]

    rows = soup.findAll('tbody')[1].findAll('tr')

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]

    res = pd.DataFrame(data, columns = headers).to_dict()
    print(res)
    return res



