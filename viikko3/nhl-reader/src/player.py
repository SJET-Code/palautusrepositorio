class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
    def __str__(self):
        return f'{self.name:25}{self.team:<2} {self.goals} + {self.assists:<2} = {self.goals+self.assists}'
