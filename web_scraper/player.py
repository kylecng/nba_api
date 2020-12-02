from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd



def url_builder(first_name,last_name):
    first_name = first_name.lower()
    last_name = last_name.lower()
    builder = ['https://www.basketball-reference.com/players/']
    builder.append(last_name[0])
    builder.append('/')
    if (len(last_name) <= 5):
        builder.append(last_name)
    else:
        builder.append(last_name[:5])
    if (len(first_name) <= 2):
        builder.append(first_name)
    else:
        builder.append(first_name[:2])
    builder.append('01.html')
    url = "".join(builder)
    # print(url)
    return url

def get_player_per_game_stats(first_name,last_name):
    url = url_builder(first_name,last_name)
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]

    rows = soup.findAll('tbody')[0].findAll('tr')

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]

    res = pd.DataFrame(data, columns = headers).to_dict(orient='index')
    res["ignoreme"] = True
    # print(res)
    return res
