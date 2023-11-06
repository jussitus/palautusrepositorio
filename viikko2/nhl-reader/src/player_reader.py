import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
        response = requests.get(url).json()
        self.players = []
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

    def get_players(self):
        return self.players
