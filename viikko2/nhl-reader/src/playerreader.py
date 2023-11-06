import requests
from player import Player

class PlayerReader:
    def __init__(self, url:str):
        self.url = url

    def get_players(self):
        self.response = requests.get(self.url).json()
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players