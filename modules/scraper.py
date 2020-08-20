from bs4 import BeautifulSoup
import requests
import re

from modules.common import Common
from modules.game import Game
from modules.team import Team
from modules.player import Player


class EspnScraper(object):
    BASE_NBA_LINK = 'https://www.espn.com/nba/'
    CHROME_HEADERS = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36"}

    def __init__(self):
        self.scoreboards_link = EspnScraper.BASE_NBA_LINK + 'scoreboard/'
        self.boxscore_link = EspnScraper.BASE_NBA_LINK + 'boxscore'
        self.games = []
        self.game_ids = []

    def populate_games(self, print_summary=False, include_completed=True):
        scores = requests.get(
            self.scoreboards_link, headers=EspnScraper.CHROME_HEADERS).text

        soup = BeautifulSoup(scores, 'lxml')
        for scoreboard in soup.find_all(class_='scoreboard'):
            game_id = scoreboard.get('id')
            if game_id:
                self.game_ids.append(game_id)

        for idx, game_id in enumerate(self.game_ids):
            print("Collecting game: " + str(idx+1))
            game = self.parse_game(self.get_game(
                game_id), include_completed=include_completed)
            if game:
                self.games.append(game)
                if print_summary:
                    game.summarize_points()
            elif include_completed:
                print("Game " + str(idx+1) +
                      " has not started\n")
            else:
                print("Game " + str(idx+1) +
                      " has ended or has not started\n")

    def get_game(self, id) -> BeautifulSoup:
        game = requests.get(
            (self.boxscore_link + "?gameId={}".format(id)), headers=EspnScraper.CHROME_HEADERS).text

        soup = BeautifulSoup(game, 'lxml')
        return soup

    def get_teams(self, game) -> list:
        return game.find_all("div", {"class": re.compile('.*gamepackage-.*-wrap.*')})

    def parse_player(self, player, team_name) -> Player:
        name = player.find(class_="abbr")
        points = player.find(class_="pts")
        assists = player.find(class_="ast")
        rebounds = player.find(class_="reb")
        minutes = player.find(class_="min")
        fg = player.find(class_="fg")
        three_pt = player.find(class_="3pt")
        return Player({
            "team": team_name,
            "name": name.text if name else "",
            "points": int(points.text) if points and points.text.isnumeric() else 0,
            "assists": int(assists.text) if assists and assists.text.isnumeric() else 0,
            "rebounds": int(rebounds.text) if rebounds and rebounds.text.isnumeric() else 0,
            "minutes": int(minutes.text) if minutes and minutes.text.isnumeric() else 0,
            "fg": fg.text if fg and re.match("[0-9]+-[0-9]+", fg.text) else "0-0",
            "3pt": three_pt.text if three_pt else "0-0"
        })

    def parse_team(self, team) -> Team:
        team_name = team.find(
            "div", {"class": re.compile('.*team-name.*')}).text
        tbl_bodies = team.find(
            "table", {"class": re.compile('.*mod-data.*')}).find_all("tbody")
        team_highlights = tbl_bodies[-1].find("tr", {"class": "highlight"})
        points = int(team_highlights.find(class_='pts').text)
        starters = [self.parse_player(player, team_name)
                    for player in tbl_bodies[0].findChildren("tr")]
        bench_players = [self.parse_player(player, team_name)
                         for player in tbl_bodies[-1].findChildren("tr", class_=lambda x: x != "highlight")]
        players = starters + bench_players

        return Team({
            "name": team_name,
            "points": points,
            "players": players
        })

    def parse_game(self, game, include_completed=True) -> Game:
        game_details = game.find(class_='status-detail').text
        if not game_details:
            return None
        elif game_details.startswith("End of"):
            game_details = game_details.replace("End of", "0:00 -")
        elif game_details == "Halftime":
            game_details = game_details.replace("Halftime", "0:00 - 2nd")
        elif game_details == "Final":
            if not include_completed:
                return None
            game_details = game_details.replace("Final", "0:00 - 4th")
        game_details = game_details.split(" - ")
        time_left = game_details[0]
        quarter = game_details[1]
        teams = [self.parse_team(team) for team in self.get_teams(game)]
        return Game({
            "teams": teams,
            "quarter": quarter,
            "time_left": time_left
        })
