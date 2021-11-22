import json
import requests

from itertools import combinations

_POSSIBLE_MOVES = 9
_BOARD_SIZE_POSITIONS = [1, 2, 3]
_MAGIC_SQUARE = (
    8,
    1,
    6,
    3,
    5,
    7,
    4,
    9,
    2,
)  # used this after finding my idea was bogus -> https://mathworld.wolfram.com/MagicSquare.html


class Tictac:
    """A game of tic-tac-toe"""

    def __init__(self):
        self.url = "http://tictac_server:8000/"

    # @property
    # def game_id(self) -> int:
    #     return self.game_id

    def view_games(self):
        url = f"{self.url}/games/"
        response = requests.request("GET", url, data="", headers="")
        response_json = json.loads(response.text)

        return json.dumps(response_json, indent=4)

    def view_moves(self, game_id):
        url = f"{self.url}/game_moves/?game_id={game_id}"
        response = requests.request("GET", url, data="", headers="")
        response_json = json.loads(response.text)

        return json.dumps(response_json, indent=4)

    def create_new_game(self):
        # replace this maybe?
        """Create a new game in the db and generate the game board"""
        url = f"{self.url}/new_game/"
        response = requests.request("POST", url, data="", headers="")

        self.game_id = int(response.text)

        self.game_board = self._generate_game_board()

        self.game_moves = [None] * _POSSIBLE_MOVES

        return response.text

    def _generate_game_board(self):
        rows = _BOARD_SIZE_POSITIONS
        columns = _BOARD_SIZE_POSITIONS

        return [(x, y) for x in rows for y in columns]

    def get_move_options(self):
        available_moves = []
        for index, position in enumerate(self.game_board):
            if self.game_moves[index] == None:
                available_moves.append((index, position))

        return available_moves

    def take_turn(self, position_id, player_is_robot=0):
        # really need to think about recording the X vs O instead of a player/robot
        self.game_moves[position_id] = player_is_robot

        # post the move to the database, return the response for validation later
        post_move_response = self._post_move_to_db(position_id, player_is_robot)

        if self.number_of_moves() >= 5:
            winner = self._check_for_winner(player_is_robot)
            # winner = False
            # print("checking for a winner")
            if winner:
                # print("return something that breaks")
                return 1
            elif not winner and self.number_of_moves() == 9:
                # print("return something that breaks with a cats game")
                return -1
                # think about setting the move counts to set a valid loop length? while still may be better (could be a few ways to do a hybrid of this)
            else:
                return 0
        else:
            return 0

    def _post_move_to_db(self, position_id, player_is_robot):
        url = f"{self.url}/make_move/"
        payload = {
            "game_id": self.game_id,
            "move_sequence": self.number_of_moves(),
            "move_position": str(self.game_board[position_id]),
            "move_position_index": position_id,
            "move_maker": player_is_robot,
        }
        response = requests.request("POST", url, data=payload, headers="")

        # response_json = json.loads(response.text)
        return response.status_code
        # return json.dumps(response_json, indent=4)

    def number_of_moves(self):
        return sum(move is not None for move in self.game_moves)

    def _check_for_winner(self, player_is_robot):
        """Checks to see if someone has won the game"""

        player_wins = False

        player_moves_list = self._get_player_moves(player_is_robot)

        for move_combination in combinations(player_moves_list, 3):
            # sum_move_number = sum(
            #     [location for move in move_combination for location in move]
            # )

            sum_move_number = sum(move_combination)

            # found out at I overlooked the obvious here in the end, leaving for conversation / improvement ideas
            # if sum_move_number % 3 == 0:
            if sum_move_number == 15:
                player_wins = True
                self.winning_combination = self._get_winning_position(move_combination)
                self.winning_player_is_robot = player_is_robot
                break
            else:
                # continue iterating combinations
                pass

        return player_wins

    def _get_player_moves(self, player_is_robot):
        """Gets a list of tuples the player has made moves in"""

        # player_move_ids = [move for move in self.game_moves if player_is_robot in move]
        player_moves = []
        for index, player in enumerate(self.game_moves):
            if player == player_is_robot:
                # player_moves.append(self.game_board[index])
                player_moves.append(_MAGIC_SQUARE[index])

        return player_moves

    def _get_winning_position(self, winning_combination):
        """Returns the winning coordinate positions"""

        winning_combination_positions = []

        for magic_number in winning_combination:
            magic_square_index = _MAGIC_SQUARE.index(magic_number)
            winning_combination_positions.append(self.game_board[magic_square_index])

        return winning_combination_positions
