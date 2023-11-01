import unittest
from statistics_service import SortBy, StatisticsService, sort_by
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

    def test_sort_by_works_for_sorting_by_points(self):
        reader = PlayerReaderStub()
        players1 = sorted(reader.get_players(), key=sort_by(SortBy.POINTS))
        players2 = sorted(reader.get_players(), key=lambda player: player.goals + player.assists)
        
        self.assertEqual(list(map(str, players1)), list(map(str, players2)))

    def test_sort_by_works_for_sorting_by_goals(self):
        reader = PlayerReaderStub()
        players1 = sorted(reader.get_players(), key=sort_by(SortBy.GOALS))
        players2 = sorted(reader.get_players(), key=lambda player: player.goals)
        
        self.assertEqual(list(map(str, players1)), list(map(str, players2)))
    
    def test_sort_by_works_for_sorting_by_assists(self):
        reader = PlayerReaderStub()
        players1 = sorted(reader.get_players(), key=sort_by(SortBy.ASSISTS))
        players2 = sorted(reader.get_players(), key=lambda player: player.assists)
        
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
        self.assertEqual(list(map(str,self.stats.top(2))), list(map(str,top2)))

    def test_top_sorts_by_points(self):
        top2 = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
        ]
        self.assertEqual(list(map(str,self.stats.top(2, SortBy.POINTS))), list(map(str,top2)))
    
    def test_top_sorts_by_goals(self):
        top2 = [
            Player("Lemieux", "PIT", 45, 54),
            #Player("Yzerman", "DET", 42, 56),
        ]
        self.assertEqual(list(map(str,self.stats.top(2, SortBy.GOALS))), list(map(str,top2)))
    
    def test_top_sorts_by_assists(self):
        top2 = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
        ]
        self.assertEqual(list(map(str,self.stats.top(2, SortBy.ASSISTS))), list(map(str,top2)))

    def test_top_raises_exception_if_given_incorrect_order(self):
        with self.assertRaises(TypeError):
            self.stats.top(2, "not even an int")