from .slotmachinegame import SlotMachineGame

# Just a simple main to start the game

def main():
    print("Welcome to the Slot Machine!")
    initial_credits = int(input("Enter the amount of credits to add to the machine: "))
    game = SlotMachineGame(initial_credits)
    game.play()

if __name__ == "__main__":
    main()