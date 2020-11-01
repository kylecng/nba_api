from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def get_table(soup):
    # html = urlopen(url)
    # soup = BeautifulSoup(html,features="html.parser")

    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
    rows = soup.findAll('tbody')[0].findAll('tr')
    data = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    table = pd.DataFrame(data, columns = headers)
    print(table)
    return table
