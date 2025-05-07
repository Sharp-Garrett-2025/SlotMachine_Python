import unittest
from unittest.mock import patch
from src.slot_machine import SlotMachine

class TestSlotMachine(unittest.TestCase):
    def setUp(self):
        self.slot_machine = SlotMachine()

    def test_spin(self):
        bet = 10
        spin_result, is_winner, winnings = self.slot_machine.spin(bet)

        # Check spin result length
        self.assertEqual(len(spin_result), 3)  # Slot machine has 3 reels
        # Check if all symbols are strings
        self.assertTrue(all(isinstance(symbol, str) for symbol in spin_result))
        # Check winnings are valid if the player wins
        if is_winner:
            self.assertEqual(winnings, bet * 10)
        else:
            self.assertEqual(winnings, 0)

    def test_check_winner(self):
        # Mock random.random to return a value less than the calculated odds
        with patch('random.random', return_value=0.05):
            spin_result = ['🍒', '🍒', '🍒']
            self.assertTrue(self.slot_machine.check_winner(spin_result, 50))  # High odds with high bet

        # Mock random.random to return a value greater than the calculated odds
        with patch('random.random', return_value=0.95):
            spin_result = ['🍒', '🍋', '🍒']
            self.assertFalse(self.slot_machine.check_winner(spin_result, 1))  # Low odds with low bet


if __name__ == "__main__":
    unittest.main()