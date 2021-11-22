import click
from random import randrange

from tictac import Tictac


@click.group()
def tictac():
    pass


@tictac.command(name="games", help="Returns all started games, order by when they were created")
def view_games():
    tictac_class = Tictac()
    click.echo(tictac_class.view_games())


@tictac.command(name="gamemoves", help="Returns all moves in a specified game")
def view_game_moves():
    game_id = click.prompt("Input a valid game ID", type=int)

    tictac_class = Tictac()
    game_moves = tictac_class.view_moves(game_id)

    click.echo(game_moves)


@tictac.command(name="newgame", help="Creates a new game and walks moves through to completion")
def new_game():
    tictac_class = Tictac()
    tictac_class.create_new_game()
    click.echo(f"playing game id: {tictac_class.game_id}")
    game_complete = 0
    while game_complete == 0:
        available_moves = tictac_class.get_move_options()

        if (tictac_class.number_of_moves() % 2) == 0:
            # player to move here
            click.echo("Possible moves:")
            for move in available_moves:
                click.echo(f"Position ID: {move[0]}, Position: {move[1]}")
            move = click.prompt(
                "Please pick a position id number for you next move", type=int
            )
            # TODO add some validation here
            game_complete = tictac_class.take_turn(position_id=move)
        else:
            # selects a random position ID from the available moves
            random_selection_id = randrange(len(available_moves))
            computer_move = available_moves[random_selection_id][0]
            game_complete = tictac_class.take_turn(position_id=computer_move, player_is_robot=1)

        if game_complete == 1:
            if tictac_class.winning_player_is_robot == 0:
                click.echo("Congratulations! You win!")
            else:
                click.echo("OOF - sorry, the computer won this time...")
            click.echo("Winning combination:")
            click.echo(tictac_class.winning_combination)
        elif game_complete == -1:
            click.echo("oh dang, nobody won... try again?")


if __name__ == "__main__":
    tictac()
