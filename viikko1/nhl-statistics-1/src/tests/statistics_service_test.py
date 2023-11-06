import unittest
from statistics_service import StatisticsService
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
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player_if_name_found(self):
        self.assertAlmostEqual(self.stats.search("Semenko"),
                               self.stats._players[0])

    def test_search_returns_none_if_name_not_found(self):
        self.assertAlmostEqual(self.stats.search("Testi"),
                               None)

    def test_returns_teams_players(self):
        self.assertAlmostEqual(self.stats.team("PIT"),
                               [self.stats._players[1]])

    def test_returns_players_in_order(self):
        self.assertEqual(self.stats.top(1),
                         [self.stats._players[4]])
