import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(100)

    def test_initial_balance(self):
        self.assertEqual(self.player.get_balance(), 100)

    def test_place_bet(self):
        bet = 10
        self.player.place_bet(bet)
        self.assertEqual(self.player.get_balance(), 90)

        # Test insufficient balance
        with self.assertRaises(ValueError) as context:
            self.player.place_bet(200)
        self.assertEqual(str(context.exception), "Insufficient balance to place this bet.")

    def test_add_winnings(self):
        self.player.add_winnings(50)
        self.assertEqual(self.player.get_balance(), 150)

    def test_get_balance(self):
        self.assertEqual(self.player.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()