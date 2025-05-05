import unittest
from src.slot_machine import SlotMachine

class TestSlotMachine(unittest.TestCase):
    def test_spin(self):
        slot_machine = SlotMachine()
        bet = 10
        spin_result, is_winner, winnings = slot_machine.spin(bet)

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
        slot_machine = SlotMachine()

        # Test winning condition with high bet
        spin_result = ['🍒', '🍒', '🍒']
        self.assertTrue(slot_machine.check_winner(spin_result, 50))  # High odds with high bet

        # Test losing condition with low bet
        spin_result = ['🍒', '🍋', '🍒']
        self.assertFalse(slot_machine.check_winner(spin_result, 1))  # Low odds with low bet

if __name__ == "__main__":
    unittest.main()