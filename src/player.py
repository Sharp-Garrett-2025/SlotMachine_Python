class Player:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def place_bet(self, bet):
        if bet > self.balance:
            raise ValueError("Insufficient balance to place this bet.")
        self.balance -= bet
        return bet

    def add_winnings(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance