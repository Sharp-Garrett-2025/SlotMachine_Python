from src.slotmachinegame import SlotMachineGame

def main():
    print("Welcome to the Slot Machine!")
    initial_credits = int(input("Enter the amount of credits to add to the machine: "))
    game = SlotMachineGame(initial_credits)
    game.play()

if __name__ == "__main__":
    main()