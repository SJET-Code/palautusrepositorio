class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1 = {'name': player1_name, 'score' : 0}
        self.player2 = {'name': player2_name, 'score' : 0}

    def won_point(self, player_name: str):
        if self.player1['name'] == player_name:
            self.player1['score'] += 1
        else:
            self.player2['score'] += 1

    def someone_won(self, scores: tuple):
        return abs(scores[0] - scores[1]) > 1 and self.advantage(scores)

    def advantage_to(self, scores: tuple):
        if scores[0] > scores[1]:
            return self.player1['name']
        return self.player2['name']

    def tie(self, scores: tuple):
        return scores[0] == scores[1]

    def advantage(self, scores: tuple):
        return scores[0] >= 4 or scores[1] >= 4

    def format_score(self, scores: tuple):
        output = {0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty"}
        if self.someone_won(scores):
            return f"Win for {self.advantage_to(scores)}"
        if self.tie(scores):
            if scores[0] < 3:
                return f"{output[scores[0]]}-All"
            return "Deuce"
        if self.advantage(scores):
            return f"Advantage {self.advantage_to(scores)}"
        return f"{output[scores[0]]}-{output[scores[1]]}"

    def get_score(self):
        return self.format_score((self.player1['score'], self.player2['score']))
