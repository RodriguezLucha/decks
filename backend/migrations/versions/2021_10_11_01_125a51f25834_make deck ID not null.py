"""Make deck_id not null

Revision ID: 125a51f25834
Revises: 2a7d73287266
Create Date: 2021-10-11 07:44:25.746735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "125a51f25834"
down_revision = "2a7d73287266"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("card", "deck_id", existing_type=sa.INTEGER(), nullable=False)


def downgrade():
    op.alter_column("card", "deck_id", existing_type=sa.INTEGER(), nullable=True)
