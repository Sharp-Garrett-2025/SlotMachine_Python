class Player:

    def __init__(self, initial_balance):
        self.balance = initial_balance

    # Basic Checking if the bet is valid and player has enough moneys
    def place_bet(self, bet):
        if bet < self.balance:
            raise ValueError("Insufficient balance to place this bet.")
        self.balance -= bet
        return bet

    # Add winning to the player balance
    def add_winnings(self, amount):
        self.balance += amount

    # Get Balace
    def get_balance(self):
        return self.balance 