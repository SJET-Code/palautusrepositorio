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
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_pelaaja_loytyy_nimella_search_metodilla(self):
        nimi = 'Gretzky'
        self.assertEqual(self.stats.search(nimi).name,nimi)

    def test_pelaajaa_ei_loydy_nimella_search_metodilla_jos_nimi_on_vaara(self):
        nimi = 'LeBron'
        self.assertEqual(self.stats.search(nimi),None)

    def test_joukkueen_pelaajat_loytyvat_joukkueen_nimella_team_metodilla(self):
        joukkue = 'EDM'
        self.assertEqual(len(self.stats.team(joukkue)), 3)

    def test_eniten_pisteita_tehneet_pelaajat_loytyvat_top_metodilla(self):
        top = self.stats.top(3)
        self.assertEqual(top[0].name + top[1].name + top[2].name, 'GretzkyLemieuxYzerman')