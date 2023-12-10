from matchers import *


class QueryBuilder:
    def __init__(self, query = []) -> None:
        self._query = query

    def playsIn(self, team):
        return QueryBuilder(self._query + [PlaysIn(team)])

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._query + [HasAtLeast(value, attr)])
    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._query + [HasFewerThan(value, attr)])
    
    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(self._query + [Or(matcher1, matcher2)])

    def build(self):
        if len(self._query) == 0:
            return All()
        return And(*self._query)
