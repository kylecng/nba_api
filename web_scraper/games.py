from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def url_builder(month,day,year):
    builder = ["https://www.basketball-reference.com/boxscores/?month="]
    builder.append(str(month))
    builder.append('&day=')
    builder.append(str(day))
    builder.append('&year=')
    builder.append(str(year))
    url = "".join(builder)
    return url

def get_games(month,day,year):
    print('get_games')
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
        data['away'] = away_data[0].getText()
        data['away_score'] = away_data[1].getText()
        data['home'] = home_data[0].getText()
        data['home_score'] = home_data[1].getText()
        res[i] = data
        i+=1
    print("HMMMM")
    print(res)
    print("LOLL")
    return res

        
def get_standings(month,day,year,conference):
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

    res = pd.DataFrame(data, columns = headers)
    res = res.to_dict
    print(res)
    return res
