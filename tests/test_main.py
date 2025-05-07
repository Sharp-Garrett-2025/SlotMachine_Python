import unittest
from unittest.mock import patch, MagicMock
from src.main import main
from src.slotmachinegame import SlotMachineGame

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['100'])  # Mock user input for initial credits
    @patch('src.main.SlotMachineGame')  # Mock the SlotMachineGame class
    def test_main(self, mock_game, mock_input):
        # Create a mock instance of SlotMachineGame
        mock_game_instance = MagicMock()
        mock_game.return_value = mock_game_instance

        # Call the main function
        main()

        # Check that SlotMachineGame was initialized with the correct credits
        mock_game.assert_called_once_with(100)

        # Check that the play method was called
        mock_game_instance.play.assert_called_once()

if __name__ == "__main__":
    unittest.main()