# NBA API

Retrieve relevant NBA player, team, and season stats. Data is webscraped from basketball-reference.com and cached in a database.

## Base URL
```
https://basketball-reference-api.herokuapp.com/
```

## Player Calls

### Player Per Game Stats

- URL
  `/players/:last_name/:first_name/per_game_stats`
- Method
  `GET`
- URL Params
  Required:
  ```
  last_name=[string]
  `first_name=[string]
  ```
- Response
  `{"0":{"Season":"2003-04","Age":"19","Tm":"CLE","Lg":"NBA","Pos":"SG","G":"79","GS":"79","MP":"39.5","FG":"7.9","FGA":"18.9","FG%":".417","3P":"0.8","3PA":"2.7","3P%":".290","2P":"7.1","2PA":"16.1","2P%":".438","eFG%":".438","FT":"4.4","FTA":"5.8","FT%":".754","ORB":"1.3","DRB":"4.2","TRB":"5.5","AST":"5.9","STL":"1.6","BLK":"0.7","TOV":"3.5","PF":"1.9","PTS":"20.9"},"1":{"Season":"2004-05","Age":"20","Tm":"CLE","Lg":"NBA","Pos":"SF","G":"80","GS":"80","MP":"42.4","FG":"9.9","FGA":"21.1","FG%":".472","3P":"1.4","3PA":"3.9","3P%":".351","2P":"8.6","2PA":"17.2","2P%":".499","eFG%":".504","FT":"6.0","FTA":"8.0","FT%":".750","ORB":"1.4","DRB":"6.0","TRB":"7.4","AST":"7.2","STL":"2.2","BLK":"0.7","TOV":"3.3","PF":"1.8","PTS":"27.2"}...}`

## Games Calls

### Game Data

- URL
  `/games/:year/:month/:day/games_data/:home_team`
- Method
  `GET`
- URL Params
  Required:
  ```
  year=[int]
  month=[int]
  day=[int]
  ```
- Response
  `{"away_team":"Los Angeles Lakers","game_location":"The Arena, Bay Lake, Florida","boxscore_home_basic_g":{"0":{"Player":"LeBron James","MP":"41:13","FG":"13","FGA":"20","FG%":".650","3P":"1","3PA":"5","3P%":".200","FT":"1","FTA":"4","FT%":".250","ORB":"3","DRB":"11","TRB":"14","AST":"10","STL":"1","BLK":"0","TOV":"1","PF":"3","PTS":"28","Plus-Minus":"+18"}...},"boxscore_home_basic_q1":{"0":{"Player":"LeBron James","MP":"10:25","FG":"4","FGA":"5","FG%":".800","3P":"0","3PA":"1","3P%":".000","FT":"1","FTA":"1","FT%":"1.000","ORB":"0","DRB":"5","TRB":"5","AST":"3","STL":"0","BLK":"0","TOV":"0","PF":"0","PTS":"9","Plus-Minus":"+7"}...}...}`

### Daily Game Scores

- URL
  `/games/:year/:month/:day/game_scores`
- Method
  `GET`
- URL Params
  Required:
  ```
  year=[int]
  month=[int]
  day=[int]
  ```
- Response
  `{"0":{"away_team":"Miami","away_score":"117","home_team":"Boston","home_score":"114"},"1":{"away_team":"Denver","away_score":"104","home_team":"LA Clippers","home_score":"89"}}`

### Yearly Game Scores

- URL
  `/games/:year/game_scores`
- Method
  `GET`
- URL Params
  Required:
  ```
  year=[int]
  ```
- Response
  `{"0":{"date":"Tue, Oct 22, 2019","away_team":"New Orleans Pelicans","away_score":"122","home_team":"Toronto Raptors","home_score":"130"},"1":{"date":"Tue, Oct 22, 2019","away_team":"Los Angeles Lakers","away_score":"102","home_team":"Los Angeles Clippers","home_score":"112"}...}`

## Team Calls

### Team Seasons Summaries

- URL
  `/teams/:team_name/seasons_summaries`
- Method
  `GET`
- URL Params
  Required:
  ```
  team_name=[string]
  ```
- Response
  `{"0":{"Season":"2020-21","Lg":"NBA","Team":"Los Angeles Lakers","W":"0","L":"0","WL%":"","Finish":"1st of 5","SRS":"","\u00a0":"","Pace":"","Rel Pace":"","ORtg":"","Rel ORtg":"","DRtg":"","Rel DRtg":"","Playoffs":"","Coaches":"","Top WS":""},"1":{"Season":"2019-20","Lg":"NBA","Team":"Los Angeles Lakers*","W":"52","L":"19","WL%":".732","Finish":"1st of 5","SRS":"6.28","\u00a0":"","Pace":"100.9","Rel Pace":"0.6","ORtg":"112.0","Rel ORtg":"1.4","DRtg":"106.3","Rel DRtg":"-4.3","Playoffs":"Won Finals","Coaches":"F. Vogel (52-19)","Top WS":"A. Davis\u00a0(11.1)"}...}`

### Team Total Stats

- URL
  `/teams/:team_name/seasons_total_stats`
- Method
  `GET`
- URL Params
  Required:
  ```
  team_name=[string]
  ```
- Response
  `{"0":{"Season":"2019-20","Lg":"NBA","Tm":"ATL","W":"20","L":"47","Finish":"5","Age":"24.1","Height":"6-6","Weight":"216","G":"67","MP":"16280","FG":"2723","FGA":"6067","FG%":".449","3P":"805","3PA":"2416","3P%":".333","2P":"1918","2PA":"3651","2P%":".525","FT":"1237","FTA":"1566","FT%":".790","ORB":"661","DRB":"2237","TRB":"2898","AST":"1605","STL":"523","BLK":"341","TOV":"1086","PF":"1548","PTS":"7488"},"1":{"Season":"2018-19","Lg":"NBA","Tm":"ATL","W":"29","L":"53","Finish":"5","Age":"25.1","Height":"6-7","Weight":"215","G":"82","MP":"19855","FG":"3392","FGA":"7524","FG%":".451","3P":"1067","3PA":"3034","3P%":".352","2P":"2325","2PA":"4490","2P%":".518","FT":"1443","FTA":"1918","FT%":".752","ORB":"955","DRB":"2825","TRB":"3780","AST":"2118","STL":"675","BLK":"419","TOV":"1397","PF":"1932","PTS":"9294"}...}`

### Team Per Game Stats

- URL
  `/teams/:team_name/per_game_stats`
- Method
  `GET`
- URL Params
  Required:
  ```
  team_name=[string]
  ```
- Response
  `{"0":{"Season":"2019-20","Lg":"NBA","Tm":"LAL","W":"52","L":"19","Finish":"1","Age":"29.5","Height":"6-6","Weight":"224","G":"71","MP":"240.7","FG":"42.3","FGA":"88.3","FG%":".480","3P":"11.0","3PA":"31.6","3P%":".349","2P":"31.3","2PA":"56.7","2P%":".552","FT":"17.7","FTA":"24.3","FT%":".729","ORB":"10.7","DRB":"35.1","TRB":"45.7","AST":"25.4","STL":"8.6","BLK":"6.6","TOV":"15.2","PF":"20.7","PTS":"113.4"},"1":{"Season":"2018-19","Lg":"NBA","Tm":"LAL","W":"37","L":"45","Finish":"4","Age":"26.2","Height":"6-7","Weight":"219","G":"82","MP":"241.2","FG":"42.6","FGA":"90.5","FG%":".470","3P":"10.3","3PA":"31.0","3P%":".333","2P":"32.2","2PA":"59.6","2P%":".541","FT":"16.3","FTA":"23.3","FT%":".699","ORB":"10.2","DRB":"36.4","TRB":"46.6","AST":"25.6","STL":"7.5","BLK":"5.4","TOV":"15.7","PF":"20.7","PTS":"111.8"}...}`

## Team Season Calls

### Team Season Game Scores

- URL
  `/teams/:team_name/:year/game_scores`
- Method
  `GET`
- URL Params
  Required:
  ```
  team_name=[string]
  year=[int]
  ```
- Response
  `{"0":{"Game Number":1,"Date":"10-22","Home Game":false,"Opponent":"LAC","Win":false,"Team Score":102,"Opponent Score":112,"Wins":0,"Losses":1},"1":{"Game Number":2,"Date":"10-25","Home Game":true,"Opponent":"UTA","Win":true,"Team Score":95,"Opponent Score":86,"Wins":1,"Losses":1}...}`

### Team Season Player Per Game Stats

- URL
  `/teams/:team_name/:year/players_per_game_stats`
- Method
  `GET`
- URL Params
  Required:
  ```
  team_name=[string]
  year=[int]
  ```
- Response
  `{"0":{"Rk":"1","Name":"LeBron James","Age":"35","G":"67","GS":"67","MP":"34.6","FG":"9.6","FGA":"19.4","FG%":".493","3P":"2.2","3PA":"6.3","3P%":".348","2P":"7.4","2PA":"13.1","2P%":".564","eFG%":".550","FT":"3.9","FTA":"5.7","FT%":".693","ORB":"1.0","DRB":"6.9","TRB":"7.8","AST":"10.2","STL":"1.2","BLK":"0.5","TOV":"3.9","PF":"1.8","PTS":"25.3"},"1":{"Rk":"2","Name":"Anthony Davis","Age":"26","G":"62","GS":"62","MP":"34.4","FG":"8.9","FGA":"17.7","FG%":".503","3P":"1.2","3PA":"3.5","3P%":".330","2P":"7.7","2PA":"14.2","2P%":".546","eFG%":".536","FT":"7.2","FTA":"8.5","FT%":".846","ORB":"2.3","DRB":"7.0","TRB":"9.3","AST":"3.2","STL":"1.5","BLK":"2.3","TOV":"2.5","PF":"2.5","PTS":"26.1"}...}`
