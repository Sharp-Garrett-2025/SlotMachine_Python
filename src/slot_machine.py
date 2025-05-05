class SlotMachine:
    def __init__(self):
        self.symbols = ['🍒', '🍋', '🍊', '🍉', '⭐']
        self.reels = [self.symbols] * 3  # Three reels

    def spin(self, bet):
        import random
        spin_result = [random.choice(reel) for reel in self.reels]
        if self.check_winner(spin_result, bet):
            winnings = bet * 10  # Example payout multiplier
            return spin_result, True, winnings
        return spin_result, False, 0

    def check_winner(self, spin_result, bet):
        # Increase odds of winning with higher bets
        odds = min(0.1 + (bet / 100), 0.9)  # Cap odds at 90%
        import random
        return random.random() < odds

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