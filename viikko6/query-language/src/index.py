from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, Not, PlaysIn


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(Not(HasAtLeast(2, "goals")), PlaysIn("NYR"))
    for player in stats.matches(matcher):
        print(player)

    matcher = And(HasFewerThan(2, "goals"), PlaysIn("NYR"))
    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
