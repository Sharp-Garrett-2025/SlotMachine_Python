import unittest
from unittest.mock import patch, MagicMock
from src.slotmachinegame import SlotMachineGame
from src.player import Player
from src.slot_machine import SlotMachine
from src.jackpot import Jackpot

class TestSlotMachineGame(unittest.TestCase):
    # Was thinking of this video the entire time i was coding this: https://www.youtube.com/shorts/C2ChiBEpdJ8

    def setUp(self):
        self.initial_credits = 100
        self.game = SlotMachineGame(self.initial_credits)

    def test_initialization(self):
        # Check initial player balance
        self.assertEqual(self.game.player.get_balance(), self.initial_credits)
        # Check last bet
        self.assertIsNone(self.game.last_bet)

    @patch('builtins.input', side_effect=['10', 'y', 'n'])  # Mock user input for bets and choices
    def test_play(self, mock_input):
        # Mock methods to avoid randommness
        self.game.slot_machine.spin = MagicMock(return_value=(['🍒', '🍒', '🍒'], True, 100))
        self.game.jackpot.contribute = MagicMock()
        self.game.player.place_bet = MagicMock()
        self.game.player.get_balance = MagicMock(return_value=100)

        # Call the play method
        self.game.play()

        # Check that the spin method was called
        self.game.slot_machine.spin.assert_called()

    def test_handle_spin(self):
        # Mock spin result
        self.game.slot_machine.spin = MagicMock(return_value=(['🍒', '🍒', '🍒'], True, 100))
        self.game.handle_spin(10)

        # Check that winnings were added
        self.assertEqual(self.game.player.get_balance(), 200)

    def test_handle_spin_win(self):
        # Simulate a winning spin
        bet = 10
        self.game.player.place_bet(bet)
        self.game.handle_spin(bet)

        # Check that the player's balance is updated correctly
        self.assertGreaterEqual(self.game.player.get_balance(), 90)

    def test_jackpot_contribution(self):
        # Simulate a bet and check jackpot contribution
        bet = 10
        self.game.player.place_bet(bet)
        self.game.jackpot.contribute(bet)

        self.assertGreater(self.game.jackpot.get_pool(), 1000)

    @patch('builtins.input', side_effect=['100', '10', 'n'])  # Mock invalid bet followed by a valid bet
    def test_invalid_bet(self, mock_input):
        # Mock methods to avoid randomness
        self.game.slot_machine.spin = MagicMock(return_value=(['🍒', '🍒', '🍒'], True, 100))
        self.game.jackpot.contribute = MagicMock()
        self.game.player.place_bet = MagicMock()

        # Call the play method
        self.game.play()

        # Check that the spin method was called after a valid bet
        self.game.slot_machine.spin.assert_called()
        
    def test_full_game_flow(self):
        # Mock methods to simulate a full game flow
        with patch('builtins.input', side_effect=['10', 'y', 'n']):  # Mock user input
            self.game.slot_machine.spin = MagicMock(return_value=(['🍒', '🍒', '🍒'], True, 100))
            self.game.jackpot.contribute = MagicMock()
            self.game.player.place_bet = MagicMock()
            self.game.player.get_balance = MagicMock(return_value=100)

            self.game.play()

            self.game.slot_machine.spin.assert_called()
            self.game.jackpot.contribute.assert_called()
            self.game.player.place_bet.assert_called()

if __name__ == "__main__":
    unittest.main()