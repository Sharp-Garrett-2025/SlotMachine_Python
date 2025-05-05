import unittest
from src.slot_machine import Player

class TestPlayer(unittest.TestCase):
    def test_initial_balance(self):
        player = Player(100)
        self.assertEqual(player.get_balance(), 100)

    def test_place_bet(self):
        player = Player(100)
        bet = 10
        player.place_bet(bet)
        self.assertEqual(player.get_balance(), 90)

        # Test insufficient balance
        with self.assertRaises(ValueError) as context:
            player.place_bet(200)
        self.assertEqual(str(context.exception), "Insufficient balance to place this bet.")

    def test_add_winnings(self):
        player = Player(100)
        player.add_winnings(50)
        self.assertEqual(player.get_balance(), 150)

    def test_get_balance(self):
        player = Player(100)
        self.assertEqual(player.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()