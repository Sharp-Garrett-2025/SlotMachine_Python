class Jackpot:
    def __init__(self, initial_amount=1000):
        self.pool = initial_amount

    def contribute(self, bet):
        # Add 5% of the bet to the jackpot pool
        self.pool += bet * 0.05

    def try_win(self):
        import random
        # 1 in 10,000 chance to win the jackpot
        if random.randint(1, 10000) == 1:
            winnings = self.pool
            self.pool = 1000  # Reset jackpot
            return winnings
        return 0

    def get_pool(self):
        return self.pool