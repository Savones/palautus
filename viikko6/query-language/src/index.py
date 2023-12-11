from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All


class QueryBuilder:

    def __init__(self, query_builder=None):
        if not query_builder:
            self.query_builder = All()
        else:
            self.query_builder = query_builder

    def build(self):
        return self.query_builder

    def hasFewerThan(self, value, thing):
        new = And(self.query_builder, HasFewerThan(value, thing))
        return QueryBuilder(new)

    def hasAtLeast(self, value, thing):
        new = And(self.query_builder, HasAtLeast(value, thing))
        return QueryBuilder(new)

    def playsIn(self, player_team):
        new = And(self.query_builder, PlaysIn(player_team))
        return QueryBuilder(new)


def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.playsIn("NYR").hasAtLeast(
        10, "goals").hasFewerThan(20, "goals").build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
