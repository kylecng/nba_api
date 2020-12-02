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
    # print(url)
    return url

# def get_team_season(team,year):
#     url = url_builder(team,year)
#     html = urlopen(url)
#     soup = BeautifulSoup(html,features="html.parser")
#     res = {}
#     res['record'] = get_season_record(team,year)
#     res['coach'] = get_coach(team,year)
#     res['executive'] = get_exec(team,year)
#     res['pace'] = get_pace(team,year)
#     res['off_rtg'] = get_off_rtg(team,year)
#     res['def_rtg'] = get_def_rtg(team,year)
#     res['arena'] = get_arena(team,year)
#     res['game_scores'] = get_game_scores(team,year)
#     res['roster_stats'] = get_roster_stats(team,year)
#     res['per_game_stats'] = get_per_game_stats(team,year)
#     return res

# ##record; wins, losses, conference standing
# def get_season_record(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).find("p").getText()
#     nums = [int(s) for s in re.split('t|-|,| ',text)if s.isdigit()]
#     res = {}
#     res["wins"] = nums[0]
#     res["losses"] = nums[1]
#     res["conference_standing"] = nums[2]
#     print(res)
#     return res



# ##Coach
# def get_coach(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[2].getText()
#     s = text.split()
#     res = s[1] + ' ' + s[2]
#     print(res)
#     return res

# ##Executive
# def get_exec(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[3].getText()
#     s = text.split()
#     res = s[1] + ' ' + s[2]
#     print(res)
#     return res

# ##pace
# def get_pace(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[5].getText()
#     s = text.split()
#     res = s[6]
#     print(res)
#     return res

# ##Off Rtg
# def get_off_rtg(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[6].getText()
#     s = text.split()
#     res = s[2]
#     print(res)
#     return res

# ##Def Rtg
# def get_def_rtg(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[6].getText()
#     s = text.split()
#     res = s[8]
#     print(res)
#     return res

# ##Arena
# def get_arena(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     text = soup.find("div", {"id":"info"}).find("div",{"data-template" : "Partials/Teams/Summary"}).findAll("p")[9].getText()
#     s = text.split()
#     res = ""
#     i = 1
#     print(s)
#     while (i < len(s) and s[i] != "Attendance:"):
#         res += s[i] + " "
#         i += 1
#     print(res)
#     return res


def get_team_season_game_scores(team,year,soup=None):
    if soup is None:
        url = url_builder(team,year)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    rowText = soup.find("div", {"id":"timeline_results"}).findAll("li",{"class":"result"})
    rowText = [s.getText() for s in rowText]
    headers = ['Game Number','Date','Home Game','Opponent','Win','Team Score','Opponent Score','Wins','Losses',]
    data = []
    for r in rowText:
        r = r.replace('(',' ').replace(')',' ').strip()
        s = re.split("-|,| ",r)
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


    res = pd.DataFrame(data, columns = headers).to_dict(orient='index')
    res["ignoreme"] = True
    # print(res)
    return res

# ##Roster Table
# def get_team_season_roster_info(team,year,soup=None):
#     if soup is None:
#         url = url_builder(team,year)
#         html = urlopen(url)
#         soup = BeautifulSoup(html,features="html.parser")
#     headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
#     rows = soup.find('tbody').findAll('tr')

#     data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
#                 for i in range(len(rows))]

#     res = pd.DataFrame(data, columns = headers).to_dict(orient='index')
#     res["ignoreme"] = True
#     # print(res)
#     return res

##Per Game Table
def get_team_season_players_per_game_stats(team,year,soup=None):
    if soup is None:
        url = url_builder(team,year)
        html = urlopen(url)
        soup = BeautifulSoup(html,features="html.parser")
    headers = [th.getText() for th in soup.findAll('table')[1].find('tr').findAll('th')]
    headers[1] = 'Name'
    headers[-1] = 'PTS'
    rows = soup.findAll('tbody')[1].findAll('tr')

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]

    res = pd.DataFrame(data, columns = headers).to_dict(orient='index')
    res["ignoreme"] = True
    # print(res)
    return res



