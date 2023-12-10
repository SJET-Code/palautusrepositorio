from matchers import All, And, Or, HasAtLeast, HasFewerThan, PlaysIn, Not

class QueryBuilder:
    def __init__(self, query = All()):
        self.query = query

    def build(self):
        return self.query
    
    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def Not(self, condition):
        return QueryBuilder(And(self.query, Not(condition)))

    def oneOf(*queries):
        or_query = [queries[1]]
        for i in range(2,len(queries)):
            or_query.append(queries[i])
        return QueryBuilder(Or(*or_query))
