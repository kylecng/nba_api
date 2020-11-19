from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

def url_builder(year,month=None,day=None):
    if day is None:
        builder = ["https://www.basketball-reference.com/leagues/NBA_"]
        builder.append(str(year))
        builder.append('_games')
        if month is not None:
            builder.append('-')
            if isinstance(month,int):
                builder.append(str(months[month]).lower())
            else:
                builder.append(month.lower())
        builder.append('.html')
    else:
        builder = ["https://www.basketball-reference.com/boxscores/?month="]
        builder.append(str(month))
        builder.append('&day=')
        builder.append(str(day))
        builder.append('&year=')
        builder.append(str(year))
    url = "".join(builder)
    print(url)
    return url

def get_game_scores_day(year,month,day):
    url = url_builder(month,day,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")

    res = {}
    games = soup.find('div',{'class':'game_summaries'})
    if not games:
        print(res)
        return res
    games = games.findAll('div',{'class': 'game_summary expanded nohover'})
    i = 0
    for game in games:
        data = {}
        game_data = game.find('tbody').findAll('tr')
        away_data = game_data[0].findAll('td')
        home_data = game_data[1].findAll('td')
        data['away_team'] = away_data[0].getText()
        data['away_score'] = away_data[1].getText()
        data['home_team'] = home_data[0].getText()
        data['home_score'] = home_data[1].getText()
        res[i] = data
        i+=1
    # print(res)
    return res

        
def get_standings(year,month,day,conference):
    url = url_builder(month,day,year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")

    i = 0
    if conference == 'E':
        i = 0
    elif conference == 'W':
        i = 1
    table = soup.find('div',{'class':'standings_confs data_grid section_wrapper'}).findAll('table')[i]
    
    headers = [th.getText() for th in table.find('tr').findAll('th')]

    rows = table.find('tbody').findAll('tr')
    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]

    res = pd.DataFrame(data, columns = headers).to_dict(orient='index')
    # print(res)
    return res



def get_game_scores_month(year,month):
    url = url_builder(year,month)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    headers = soup.find('table').find('tr').findAll('th')
    headers = [headers[i].getText() for i in range(len(headers))]
    headers[0] = 'date'
    headers[2] = 'away_team'
    headers[3] = 'away_score'
    headers[4] = 'home_team'
    headers[5] = 'home_score'
    rows = soup.findAll('tbody')[0].findAll('tr')

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    exclude = {1,6,7,8,9}
    res = pd.DataFrame(data, columns = headers).drop(columns=[headers[i] for i in exclude]).to_dict(orient='record')
    # print(res)
    return res


def get_game_scores_season(year):
    url = url_builder(year)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    season_months = [season_month.getText().strip('\n\t').lower() for season_month in soup.find('div',{'role':'main'}).find('div',{'class':'filter'}).findAll('div')]
    print(season_months)
    res = {}
    res["ignoreme"] = True
    i = 0
    for season_month in season_months:
        for game in get_games_month(year,season_month):
            res[i] = game
            i+=1
    # print(res)
    return res
