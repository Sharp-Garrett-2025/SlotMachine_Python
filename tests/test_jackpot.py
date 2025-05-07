import unittest
from src.jackpot import Jackpot

class TestJackpot(unittest.TestCase):
    def setUp(self):
        self.jackpot = Jackpot(initial_amount=1000)

    def test_initial_pool(self):
        self.assertEqual(self.jackpot.get_pool(), 1000)

    def test_contribute(self):
        self.jackpot.contribute(100)
        self.assertEqual(self.jackpot.get_pool(), 1005)  # 5% of 100 added

    def test_try_win(self):
        # Simulate a win
        self.jackpot.pool = 5000
        winnings = self.jackpot.try_win()
        if winnings > 0:
            self.assertEqual(winnings, 5000)
            self.assertEqual(self.jackpot.get_pool(), 1000)  # Jackpot resets
        else:
            self.assertEqual(self.jackpot.get_pool(), 5000)  # No win, pool remains the same

if __name__ == "__main__":
    unittest.main()