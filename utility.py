from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import asyncio

def get_table(soup):
    # html = urlopen(url)
    # soup = BeautifulSoup(html,features="html.parser")

    headers = [th.getText() for th in soup.find('table').find('tr').findAll('th')]
    rows = soup.findAll('tbody')[0].findAll('tr')
    stats = [[td.getText() for td in [rows[i].find('th')] +  rows[i].findAll('td')]
                for i in range(len(rows))]
    table = pd.DataFrame(stats, columns = headers)
    table.head(10)
    print(table)
    return table
