from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/players/a/abdulka01.html"
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")


# use findALL() to get the column headers
soup.findAll('tr', limit=2)

# use getText()to extract the text we need into a list
# headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis



# avoid the first header row
headers = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
rows = soup.findAll('tr')
# print(rows)
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
print(player_stats)

# stats = pd.DataFrame(player_stats, columns = headers)
# stats.head(10)


