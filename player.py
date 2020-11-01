from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/players/j/jamesle01.html"

html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")
# print(soup.getText())

def get_stats():
    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]

    rows = soup.findAll('tbody')[0].findAll('tr')

    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]

    stats = pd.DataFrame(data, columns = headers)
    print(stats)
    return stats


