from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import asyncio
import re

url = "https://www.basketball-reference.com/teams/ATL/2020.html"

html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")
# print(soup.getText())

# headers = [th.getText() for th in soup.findAll('table')[1].find('tr').findAll('th')]
# print(headers)

# rows = soup.findAll('tbody')[1].findAll('tr')
# print(rows)

# player_stats = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
#             for i in range(len(rows))]
# print(player_stats)

# stats = pd.DataFrame(player_stats, columns = headers)
# stats.head(10)
# print(stats)





##record; wins, losses, conference standing
def get_record():
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).find("p").getText()
    nums = [int(s) for s in re.split('t|-|,| ',text)if s.isdigit()]
    res = {}
    res["wins"] = nums[0]
    res["losses"] = nums[1]
    res["rank"] = nums[2]
    print(res)
    return res



##Coach
def get_coach():
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[2].getText()
    s = text.split()
    res = s[1] + ' ' + s[2]
    print(res)
    return res

##Executive
def get_exec():
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[3].getText()
    s = text.split()
    res = s[1] + ' ' + s[2]
    print(res)

##pace
def get_pace():
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[5].getText()
    s = text.split()
    res = s[6]
    print(res)
    return res

##Off Rtg
def get_off_rtg():
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[6].getText()
    s = text.split()
    res = s[2]
    print(res)
    return res
##Def Rtg
def get_def_rtg():
    text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[6].getText()
    s = text.split()
    res = s[8]
    print(res)
    return res
##Arena
def get_arena():
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
def get_team_games():
    rowText = soup.find("div", {"id":"timeline_results"}).findAll("li",{"class":"result"})
    rowText = [s.getText() for s in rowText]
    for row in rowText:
        
        s = re.split("-| (|) |,| ",row)
        print(s)
        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        res = {}
        res["month"] = months[s[2]]
        res["day"] = s[4]
        res["home"] = not s[6] == '@'
        # if res["home"]: 
        #     res["opp"] = s[8]
        #     res["wins"] = 
        #     res["losses"] = 
        #     res["team_score"] = 
        #     res["opp_score"] = 
        #     res["result"] = 
        # else:

        
get_team_games()

##Roster Table
def get_roster():
    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]

    rows = soup.find('tbody').findAll('tr')

    player_stats = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]

    stats = pd.DataFrame(player_stats, columns = headers)
    stats.head(10)
    print(stats)
    return stats

##Injuries???

##Per Game Table
def get_per_game():
    headers = [th.getText() for th in soup.findAll('table')[1].find('tr').findAll('th')]
    print(headers)

    rows = soup.findAll('tbody')[1].findAll('tr')
    print(rows)

    player_stats = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    print(player_stats)

    stats = pd.DataFrame(player_stats, columns = headers)
    stats.head(10)
    print(stats)




