# SlotMachine_Python/src/main.py

def main():
    from slot_machine import SlotMachine, Player

    print("Welcome to the Slot Machine!")
    
    # Initialize player with custom credits
    while True:
        try:
            initial_credits = int(input("Enter the amount of credits to add to the machine: "))
            if initial_credits <= 0:
                raise ValueError("Credits must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    player = Player(initial_credits)
    slot_machine = SlotMachine()
    allowed_bets = [1, 5, 10, 20, 50]  # Predefined bet amounts

    # Start the game loop
    while True:
        print(f"Your current balance: ${player.get_balance()}")
        play = input("Do you want to spin the slot machine? (y/n): ").strip().lower()
        if play != 'y':
            print("Thanks for playing!")
            break

        # Get the bet amount
        while True:
            try:
                bet = int(input(f"Enter your bet amount ({', '.join(map(str, allowed_bets))}): "))
                if bet not in allowed_bets:
                    raise ValueError(f"Bet must be one of the following: {', '.join(map(str, allowed_bets))}.")
                player.place_bet(bet)
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

        # Spin the slot machine
        spin_result, is_winner, winnings = slot_machine.spin(bet)
        print(f"You spun: {spin_result}")

        if is_winner:
            print(f"Congratulations! You won ${winnings}!")
            player.add_winnings(winnings)
        else:
            print("Sorry, better luck next time!")

        # Check if the player has run out of credits
        if player.get_balance() <= 0:
            print("You have run out of credits. Game over!")
            break

if __name__ == "__main__":
    main()