from src.slot_machine import SlotMachine
from src.player import Player
from src.jackpot import Jackpot

class SlotMachineGame:
    def __init__(self, initial_credits):
        self.player = Player(initial_credits)
        self.slot_machine = SlotMachine()
        self.jackpot = Jackpot()
        self.allowed_bets = [1, 5, 10, 20, 50]
        self.last_bet = None

    def handle_spin(self, bet):
        spin_result, is_winner, winnings = self.slot_machine.spin(bet)
        print(f"You spun: {spin_result}")

        # Add regular winnings
        if is_winner:
            print(f"Congratulations! You won ${winnings}!")
            self.player.add_winnings(winnings)
        else:
            print("Sorry, better luck next time!")

    def play(self):
        while True:
            print(f"Your current balance: ${self.player.get_balance()}")
            print(f"Current jackpot pool: ${self.jackpot.get_pool()}")

            # Ask the player if they want to spin
            if self.last_bet is not None:
                spin_choice = input(f"Do you want to spin the slot machine with the same bet (${self.last_bet})? (y/change/no): ").strip().lower()
                if spin_choice == 'y':
                    bet = self.last_bet
                    self.player.place_bet(bet)  # Deduct the bet amount for repeated spins
                    self.jackpot.contribute(bet)
                elif spin_choice == 'change':
                    self.last_bet = None  # Reset last bet to allow a new bet
                else:
                    print("Thanks for playing!")
                    break

            if self.last_bet is None:
                while True:
                    try:
                        bet = int(input(f"Enter your bet amount ({', '.join(map(str, self.allowed_bets))}): "))
                        if bet not in self.allowed_bets:
                            raise ValueError(f"Bet must be one of the following: {', '.join(map(str, self.allowed_bets))}.")
                        self.player.place_bet(bet)  # Deduct the bet amount for new spins
                        self.jackpot.contribute(bet)
                        self.last_bet = bet  # Store the current bet as the last bet
                        break
                    except ValueError as e:
                        print(f"Invalid input: {e}")

            # Spin the slot machine
            self.handle_spin(bet)

            # Check if the player has run out of credits
            if self.player.get_balance() <= 0:
                print("You have run out of credits. Game over!")
                break