import unittest
from statistics_service import StatisticsService, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_sort_by_points_works_for_sorting_a_list(self):
        players1 = PlayerReaderStub()
        players1 = sorted(players1.get_players(), key=sort_by_points)
        players2 = PlayerReaderStub()
        players2 = sorted(players2.get_players(), key=lambda player: player.goals + player.assists)
        
        self.assertEqual(list(map(str, players1)), list(map(str, players2)))

    def test_search_finds_player(self):
        player = Player("Lemieux", "PIT", 45, 54)
        self.assertEqual(str(self.stats.search("Lemieux")), str(player))
    
    def test_search_returns_none_for_nonexisting_player(self):
        self.assertEqual(self.stats.search("Selänne"), None)

    def test_team_finds_all_in_team(self):
        team = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89),
        ]
        self.assertEqual(list(map(str,self.stats.team("EDM"))), list(map(str,team)))
    
    def test_top_returns_top_2(self):
        top2 = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
        ]
        # top on 0-indeksoitu
        self.assertEqual(list(map(str,self.stats.top(1))), list(map(str,top2)))


        
