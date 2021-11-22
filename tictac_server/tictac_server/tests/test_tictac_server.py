import requests

import pytest


ROOT_URL = "http://tictac_server:8000/"


def test_get_games():
    url = f"{ROOT_URL}/games/"
    request = requests.get(url)

    assert request.status_code == 200

def test_get_game_moves():
    url = f"{ROOT_URL}/game_moves?game_id=1"
    request = requests.get(url)

    assert request.status_code == 200

def test_get_game_moves_bad_input():
    url = f"{ROOT_URL}/game_moves?game_id=bbb"
    request = requests.get(url)

    assert request.status_code == 500

def test_new_game_creation():
    url = f"{ROOT_URL}/new_game/"
    request = requests.post(url)

    assert request.status_code == 200
    # assert the game ID int is returned
    assert isinstance(int(request.text), int)

def test_make_move():
    url = f"{ROOT_URL}/new_game/"
    payload = {
        "game_id": 999,
        "move_sequence": 1,
        "move_position": "(3,1)",
        "move_position_index": 7,
        "move_maker": 0,
    }
    request = requests.post(url)

    assert request.status_code == 200
    # assert the move ID int is returned
    assert isinstance(int(request.text), int)
