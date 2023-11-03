from player import Player

import requests
from player import Player

def score(player:Player):
    return player.goals+player.assists

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []
    nationality = 'FIN'

    for player_dict in response:
        if player_dict['nationality'] == nationality:
            player = Player(player_dict)
            players.append(player)
    players.sort(key=score, reverse=True)
    print(f"Players from {nationality}\n")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()