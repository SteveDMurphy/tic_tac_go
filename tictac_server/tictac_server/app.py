import random

from datetime import datetime

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://tictac:tictac@tictac_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "heart_of_gold"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

## Models
class Game(db.Model):

    __tablename__ = "games"

    game_id = db.Column(db.Integer,
                   primary_key=True)
    game_state = db.Column(db.Integer,
                     index=False,
                     nullable=False)
    game_modified_at = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)

    def __init__(self):
        self.game_state = 0
        self.game_modified_at = datetime.utcnow()

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"game_id": self.game_id, "game_complete": self.game_state, "modified_at": self.game_modified_at}

class Move(db.Model):

    __tablename__ = "moves"

    move_id = db.Column(db.Integer,
                   primary_key=True)
    game_id = db.Column(db.Integer,
                     index=False,
                     nullable=False) # should have a foreign key
    move_sequence = db.Column(db.Integer,
                     index=False,
                     nullable=False)
    move_position = db.Column(db.String,
                     index=False,
                     nullable=False)
    move_position_index = db.Column(db.Integer,
                     index=False,
                     nullable=False)
    move_maker = db.Column(db.Integer,
                     index=False,
                     nullable=False) # rename this column to is_computer_move or something
    move_at = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)

    def __init__(self, game_id, move_sequence, move_position, move_position_index, move_maker):
        self.game_id = game_id
        self.move_sequence = move_sequence
        self.move_position = move_position
        self.move_position_index = move_position_index
        self.move_maker = move_maker
        self.move_at = datetime.utcnow()

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {
            "move_id": self.move_id,
            "game_id": self.game_id,
            "move_sequence": self.move_sequence,
            "move_position": self.move_position,
            "move_position_index": self.move_position_index,
            "move_maker": self.move_maker,
            "move_at": self.move_at
        }

## Endpoints

@app.route("/new_game/", methods=["GET", "POST"])
def create_game():
    """Creates a new game and returns the ID from the database"""

    new_game = Game()
    db.session.add(new_game)
    db.session.commit()

    db.session.refresh(new_game)
    # returning the id gave me some headaches
    # https://stackoverflow.com/questions/1316952/sqlalchemy-flush-and-get-inserted-id

    return jsonify(new_game.game_id)

## Add another route to update the game for state and times if you have time (add things like winner, etc. maybe?)

@app.route("/make_move/", methods=["GET", "POST"])
def make_move():
    """Posts a validated move to the database, returning the inserted ID"""

    if request.method == "POST":
        game_id = request.form.get("game_id")
        move_sequence = request.form.get("move_sequence")
        move_position = request.form.get("move_position")
        move_position_index = request.form.get("move_position_index")
        move_maker = request.form.get("move_maker")

    new_move = Move(game_id, move_sequence, move_position, move_position_index, move_maker)

    db.session.add(new_move)
    db.session.commit()

    db.session.refresh(new_move)

    return jsonify(new_move.move_id)


@app.route("/games/", methods=["GET"])
def get_games():
    """Returns the list of games played, in the order they were played."""
    game_list = Game.query.order_by(Game.game_modified_at.asc()).all()

    app.logger.debug(game_list)

    return jsonify([game.serialize for game in game_list])


@app.route("/game_moves/")
def game_moves():
    """Returns the list of moves played within a game, in the order they were played."""

    move_game_id = request.args.get("game_id")

    moves_in_game = Move.query.order_by(Move.move_at.asc()).filter_by(game_id=move_game_id)

    return jsonify([move.serialize for move in moves_in_game])


app.run(host="0.0.0.0", port=8000)

# This saved me some headaches
# https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues
