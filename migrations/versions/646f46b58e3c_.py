"""empty message

Revision ID: 646f46b58e3c
Revises: 50b719dcdb18
Create Date: 2022-03-17 05:10:05.978728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "646f46b58e3c"
down_revision = "50b719dcdb18"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("project", "equipment_id")
    op.add_column("well", sa.Column("equipment_id", sa.Integer(), nullable=True))
    pass


def downgrade():
    op.add_column("project", sa.Column("equipment_id", sa.Integer(), nullable=True))
    op.drop_column("well", "equipment_id")
    pass
