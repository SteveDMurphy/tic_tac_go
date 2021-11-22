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


### Remaining Challenge Delivery Items

* _How to run your project (or where it is hosted)_
    * (above)
* _How much time you spent building the project_
    * Time spent broke down to be roughly:
        * ~30 minutes on research on how and what I wanted to do (did this earlier in the week)
        * ~1 hour setting up and testing the services in docker-compose
        * ~3-4 hours split over Saturday and Sunday
        * Some extra time cleaning up with a fresh brain and answering these questions Monday morning.
* _Any assumptions you made_
    * I wanted to focus on delivering something that made it really easy to get up and running with very few steps so I invested some time there up front.
* _Any trade-offs you made_
    * Mainly I wanted to focus on having the game work, leaving things like visualizing the board and some further validation steps on user inputs, etc. to be filled in later if time allowed.
    * I left some of the gameplay handling in the CLI that I think would have been better served as methods in the game class, but in the end I ran out of time to refactor that
* _Any special/unique features you added_
    * I don't know that it was special, but I wanted to use this to learn a bit about the Click package as well. I have been lucky enough to use a number of lovely CLI tools over the years but have not created one from scratch before. It was a new area of my brain to scratch!
* _Anything else you want us to know about_
    * I was sitting at the vet's office Saturday morning stewing about this challenge and realized I could make a coordinate system that allowed the sum of all coordinates to be a multiple of three. It didn't work but it set me down the right path so that changes to make it work were fairly simple
* _Any feedback you have on this technical challenge..._
    * Overall I really enjoyed it! I think it was a good balance of being vague enough to let people be creative while still clear enough to get something valuable out of it (fingers crossed anyways)
    * Trying to keep within the time constraints as much as possible, but with more time (or starting again) I would focus on the following:
        * Much more focus on the gameplay and validation of steps, I ended up with limited time left and me scrambling a bit with a lack of finishing quality.
        * Earlier/better testing of the algorithm I initially came up with to determine a winner. Thankfully it was minimal rework to get to a valid result
        * Finish the planned steps around capturing game status, and being able to pick up an incomplete game
        * Build some full game testing and just improve testing in general
        * Better board visualization and visibility around moves made by the computer
        * Have a better name for the repo I created :)
