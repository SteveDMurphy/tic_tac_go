# Tic-Tac-Go!
A tic-tac-toe game using Flask, Postgres, and Click!

This game is comprised of three services, a database, a server (Flask API), and a CLI for gameplay

To get up and playing, ensure you have Docker Desktop and Make installed. Built and tested with Python 3.8

### Get Set Up

To get started, run the following commands:

`make init-db` - initializes and runs database migrations required for the application

`make tictac` - spins up the database, api, and application services - leaving you with the CLI.

### Gameplay

The game is initiated by the command `tictac newgame`

You will make the first move by selecting a position from the board of available moves (e.g 1, 7, etc.)

The computer will then make a random move before it is your turn again, repeating until either a winner is declared or every square is full.

_Determining a winner:_ Once a player has the minimum number of moves, a validation routine using a magic square is called checking all possible combinations of moves.

After playing a game (or games) to see previous matches use the `tictac games` command which will return all played games, sorted by when they were created.

To view the moves within a game, use the `tictac moves` command, entering a valid `game_id` when prompted. The `game_id` is returned either via the `tictac games` command or at the beginning of gameplay.


### Testing

`make test-tictac-server` - Runs some happy path tests for the API

`make test-tictac` - Runs some happy path tests for the cli

Some static typing effort was thrown in but not fully vetter or executed through mypy as well


### additional thoughts

Trying to keep within the time constraints as much as possible, but with more time (or starting again) I would focus on the following:

* Much more focus on the gameplay and validation of steps, leaving that until the end with limited time left me scrambling a bit with a lack of finishing quality.
* Earlier testing of the algorithm I initially came up with to determine a winner. Thankfully it was minimal rework to get to a valid result
* Finish the planned steps around capturing game status, and being able to pick up an incomplete game
* Build some full game testing and just improve testing in general
* Better board visualization and visibility around moves made by the computer
* Have a better name for it :)

In the end I really liked the game and how I approached it in general! Also I hadn't really used the Click package before so enjoyed learning a bit about that.
