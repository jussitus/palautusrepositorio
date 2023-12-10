from matchers import *
class QueryBuilder:
    def __init__(self) -> None:
        self._query = []

    def playsIn(self, team):
        self._query.append(PlaysIn(team))
        return self
    def hasAtLeast(self, value, attr):
        self._query.append(HasAtLeast(value,attr))
        return self
    def hasFewerThan(self, value, attr):
        self._query.append(HasFewerThan(value,attr))
        return self
    
    def build(self):
        if len(self._query) == 0:
            return All()
        return And(*self._query)
    