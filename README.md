# SlotMachine_Python
For the CS333 final project.

## Project Structure
```
SlotMachine_Python
├── src
│   ├── jackpot.py           # Handles jackpot contributions and payouts
│   ├── main.py              # Entry point for the application
│   ├── player.py            # Manages player credits and bets
│   ├── slot_machine.py      # Simulates the slot machine spins
│   ├── slotmachinegame.py   # Main game logic
├── tests
│   ├── test_jackpot.py          # Unit tests for the Jackpot class
│   ├── test_main.py             # Tests for the main function
│   ├── test_player.py           # Unit tests for the Player class
│   ├── test_slot_machine.py     # Unit tests for the SlotMachine class
│   ├── test_slotmachinegame.py  # Integration tests for the SlotMachineGame class
├── requirements.txt        # Lists project dependencies
├── .gitignore              # Specifies files to ignore in version control
└── README.md               # Documentation for the project
```

## Requirements
To run this project, you need to install the required dependencies. You can do this by running:
```
pip install -r requirements.txt
```

## Running the Application
To start the slot machine game, run the following command:
```
python src/main.py
```

## Running Tests
To run all unit tests, use the following command:
```
python -m unittest discover -s tests
```

## Test Coverage
```
Name                     Stmts   Miss  Cover
--------------------------------------------
src\jackpot.py              14      3    79%
src\main.py                  8      1    88%
src\player.py               12      0   100%
src\slot_machine.py         15      2    87%
src\slotmachinegame.py      47      3    94%
--------------------------------------------
TOTAL                       96      9    91%
```
