from matchers import All, And, Or, HasAtLeast, HasFewerThan, PlaysIn, Not

class QueryBuilder:
    def __init__(self, querry = All()):
        self.querry = querry

    def build(self):
        return self.querry
    
    def playsIn(self, team):
        return QueryBuilder(And(self.querry, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.querry, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.querry, HasFewerThan(value, attr)))

    def Not(self, condition):
        return QueryBuilder(And(self.querry, Not(condition)))
