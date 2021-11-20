"""create game and move tables

Revision ID: f773046a5cca
Revises:
Create Date: 2021-11-20 21:35:21.685649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f773046a5cca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    games = op.create_table(
        "games",
        sa.Column("game_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("game_state", sa.Integer, nullable=False),
        sa.Column(
            "game_modified_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    moves = op.create_table(
        "moves",
        sa.Column("move_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("game_id", sa.Integer, nullable=False),
        sa.Column("move_sequence", sa.Integer, nullable=False),
        sa.Column("move_position", sa.String(50), nullable=False),
        sa.Column("move_position_index", sa.Integer, nullable=False),
        sa.Column("move_maker", sa.Integer, nullable=False),
        sa.Column(
            "move_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

def downgrade():
    pass
