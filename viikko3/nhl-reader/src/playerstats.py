from playerreader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader:PlayerReader):
        self.reader = reader

    def score(self, player:Player):
        return player.goals+player.assists

    def top_scorers_by_nationality(self, nat:str):
        players = []
        for player in self.reader.get_players():
            if player.nationality == nat:
                players.append(player)
        players.sort(key=self.score, reverse=True)
        return players