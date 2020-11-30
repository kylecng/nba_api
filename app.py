import flask
from flask import request
import web_scraper.game as game
import web_scraper.games as games
import web_scraper.player as player
import web_scraper.season as season
import web_scraper.seasons as seasons
import web_scraper.team_season as team_season
import web_scraper.team as team
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from secrets import *
from datetime import datetime

# Fetch the service account key JSON file contents
cred = credentials.Certificate('service_account_key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': database_url
})


app = flask.Flask(__name__)
app.config["DEBUG"] = False

app.config['JSON_SORT_KEYS'] = False



@app.route('/', methods=['GET'])
def home():
    return 'Basketball Reference API'

@app.route('/games/<int:year>/<int:month>/<int:day>/games_data/<home_team>', methods=['GET'])
def get_game(year,month,day,home_team):
    print('HMMMMMMMMMMMMMMMMMM')
    ref = db.reference(request.path)
    res = ref.get()
    if (res == None):
        res = game.get_game(year,month,day,home_team)
    ref.set(res)
    return res




@app.route('/games/<int:year>/<int:month>/<int:day>/game_scores', methods=['GET'])
def get_game_scores_day(year,month,day):
    ref = db.reference(request.path)
    res = ref.get()
    if (res == None):
        res = games.get_game_scores_day(year,month,day)
    ref.set(res)
    return res


@app.route('/games/<int:year>/game_scores', methods=['GET'])
def get_game_scores_season(year):
    ref = db.reference(request.path)
    res = ref.get()
    if (res == None) or year + 1 >= datetime.today().year:
        res = games.get_game_scores_season(year)
    ref.set(res)
    return res



@app.route('/players/<last_name>/<first_name>/per_game_stats', methods=['GET'])
def get_player_per_game_stats(first_name,last_name):
    ref = db.reference(request.path)
    res = ref.get()
    if (res == None):
        res = player.get_player_per_game_stats(first_name,last_name)
    ref.set(res)
    return res







##get team season
@app.route('/teams/<team>/seasons/<int:year>', methods=['GET'])
def get_team_season(team,year):
    ref = db.reference(request.path)
    res = ref.get()
    if (res == None):
        res = team_season.get_team_season(team,year)
    ref.set(res)
    return res





##get team
@app.route('/team/<team>', methods=['GET'])
def get_team(team):
    ref = db.reference(request.path)
    res = ref.get()
    if (res == None):
        res = team.get_team(team)
    ref.set(res)
    return res




if __name__ == '__main__':
    app.run()