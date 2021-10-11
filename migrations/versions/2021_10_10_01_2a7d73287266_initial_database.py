"""Initial database creation

Revision ID: 2a7d73287266
Revises: 
Create Date: 2021-10-10 16:41:48.386649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2a7d73287266"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "deck",
        sa.Column("deck_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=True),
        sa.Column("modified_date", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("deck_id"),
    )
    op.create_table(
        "card",
        sa.Column("card_id", sa.Integer(), nullable=False),
        sa.Column("deck_id", sa.Integer(), nullable=True),
        sa.Column("num", sa.Integer(), nullable=True),
        sa.Column("name", sa.Text(), nullable=True),
        sa.Column("front_svg", sa.Text(), nullable=True),
        sa.Column("back_svg", sa.Text(), nullable=True),
        sa.Column("back_audio", sa.LargeBinary(), nullable=True),
        sa.Column("hidden", sa.Boolean(), nullable=True),
        sa.Column("modified_date", sa.DateTime(), nullable=True),
        sa.Column("last_practice_date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["deck_id"], ["deck.deck_id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("card_id"),
    )


def downgrade():
    op.drop_table("card")
    op.drop_table("deck")
