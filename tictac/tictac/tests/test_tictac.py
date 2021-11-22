import pytest

from tictac import Tictac

def test_create_new_game():

    tictac_class = Tictac()
    tictac_class.create_new_game()

    assert isinstance(int(tictac_class.game_id), int)

def test_valid_board():
    tictac_class = Tictac()
    valid_game_board = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

    assert tictac_class._generate_game_board() == valid_game_board

def test_valid_win():
    # test other options?
    tictac_class = Tictac()
    tictac_class.game_moves = [0, 0, 0]
    tictac_class.game_board = tictac_class._generate_game_board()
    move_combination = tictac_class._check_for_winner(player_is_robot=0)
    assert move_combination == True

def test_full_game():

    assert 1 == 1
