import flask
import web_scraper.game as game
import web_scraper.games as games
import web_scraper.player as player
import web_scraper.season as season
import web_scraper.seasons as seasons
import web_scraper.team_season as team_season
import web_scraper.team as team







app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/game/get_away_team/<int:year>/<int:month>/<int:day>/<home_team>', methods=['GET'])
def get_away_team(year,month,day,home_team):
    return game.get_away_team(year,month,day,home_team)

@app.route('/game/get_location/<int:year>/<int:month>/<int:day>/<home_team>', methods=['GET'])
def get_location(year,month,day,home_team):
    return game.get_location(year,month,day,home_team)

@app.route('/game/get_game_table/<int:year>/<int:month>/<int:day>/<home_team>/<team>/<stats>/<time>', methods=['GET'])
def get_game_table(year,month,day,home_team,team,stats,time):
    return game.get_game_table(year,month,day,home_team,team,stats,time)



@app.route('/games/get_games/<int:month>/<int:day>/<int:year>', methods=['GET'])
def get_games(month,day,year):
    return games.get_games(month,day,year)

@app.route('/games/get_standings/<int:month>/<int:day>/<int:year>/<conference>', methods=['GET'])
def get_standings(month,day,year,conference):
    return games.get_standings(month,day,year,conference)



@app.route('/player/get_player_stats/<first_name>/<last_name>', methods=['GET'])
def get_player_stats(first_name,last_name):
    return player.get_player_stats(first_name,last_name)




@app.route('/season/get_champion/<int:year>', methods=['GET'])
def get_champion(year):
    return season.get_champion(year)

@app.route('/season/get_mvp/<int:year>', methods=['GET'])
def get_mvp(year):
    return season.get_mvp(year)

@app.route('/season/get_roy/<int:year>', methods=['GET'])
def get_roy(year):
    return season.get_roy(year)

@app.route('/season/get_ppg_leader/<int:year>', methods=['GET'])
def get_ppg_leader(year):
    return season.get_ppg_leader(year)

@app.route('/season/get_rpg_leader/<int:year>', methods=['GET'])
def get_rpg_leader(year):
    return season.get_rpg_leader(year)

@app.route('/season/get_apg_leader/<int:year>', methods=['GET'])
def get_apg_leader(year):
    return season.get_apg_leader(year)

@app.route('/season/get_ws_leader/<int:year>', methods=['GET'])
def get_ws_leader(year):
    return season.get_ws_leader(year)









@app.route('/seasons/get_seasons', methods=['GET'])
def get_seasons():
    return seasons.get_seasons()




@app.route('/team_season/get_record/<team>/<int:year>', methods=['GET'])
def get_record(team,year):
    return team_season.get_record(team,year)

@app.route('/team_season/get_coach/<team>/<int:year>', methods=['GET'])
def get_coach(team,year):
    return team_season.get_coach(team,year)

@app.route('/team_season/get_exec/<team>/<int:year>', methods=['GET'])
def get_exec(team,year):
    return team_season.get_exec(team,year)

@app.route('/team_season/get_pace/<team>/<int:year>', methods=['GET'])
def get_pace(team,year):
    return team_season.get_pace(team,year)

@app.route('/team_season/get_off_rtg/<team>/<int:year>', methods=['GET'])
def get_off_rtg(team,year):
    return team_season.get_off_rtg(team,year)

@app.route('/team_season/get_def_rtg/<team>/<int:year>', methods=['GET'])
def get_def_rtg(team,year):
    return team_season.get_def_rtg(team,year)

@app.route('/team_season/get_arena/<team>/<int:year>', methods=['GET'])
def get_arena(team,year):
    return team_season.get_arena(team,year)

@app.route('/team_season/get_team_games/<team>/<int:year>', methods=['GET'])
def get_team_games(team,year):
    return team_season.get_team_games(team,year)

@app.route('/team_season/get_roster/<team>/<int:year>', methods=['GET'])
def get_roster(team,year):
    return team_season.get_roster(team,year)

@app.route('/team_season/get_per_game/<team>/<int:year>', methods=['GET'])
def get_per_game(team,year):
    return team_season.get_per_game(team,year)
    




@app.route('/team/get_location/<team>', methods=['GET'])
def get_location(team):
    return team.get_location(team)

@app.route('/team/get_team_names/<team>', methods=['GET'])
def get_team_names(team):
    return team.get_team_names(team)

@app.route('/team/get_num_seasons/<team>', methods=['GET'])
def get_num_seasons(team):
    return team.get_num_seasons(team)

@app.route('/team/get_record/<team>', methods=['GET'])
def get_record(team):
    return team.get_record(team)

@app.route('/team/get_num_playoffs/<team>', methods=['GET'])
def get_num_playoffs(team):
    return team.get_num_playoffs(team)

@app.route('/team/get_num_champs/<team>', methods=['GET'])
def get_num_champs(team):
    return team.get_num_champs(team)

@app.route('/team/get_num_champs/<team>', methods=['GET'])
def get_num_champs(team):
    return team.get_num_champs(team)




app.run()