"""Add new columns front text, back text, category

Revision ID: 002d30a957a0
Revises: 125a51f25834
Create Date: 2021-10-17 18:57:13.768468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "002d30a957a0"
down_revision = "125a51f25834"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("card", sa.Column("back_text", sa.Text(), nullable=True))
    op.add_column("card", sa.Column("category", sa.Text(), nullable=True))
    op.add_column("card", sa.Column("front_text", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("card", "front_text")
    op.drop_column("card", "category")
    op.drop_column("card", "back_text")
