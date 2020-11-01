from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/leagues/"

html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")
# print(soup.find('table'))

def get_seasons():
    headers = [th.getText() for th in soup.find('table').findAll('tr')[1].findAll('th')]
    print(headers)
    rows = soup.find('table').findAll('tr')[2:]
    # print(rows)

    for row in rows:
        print(row.getText())

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    # print(data)
    seasons = pd.DataFrame(data, columns = headers)
    print(seasons)
    # return stats
get_seasons()