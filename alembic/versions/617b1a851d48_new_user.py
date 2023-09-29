"""new user

Revision ID: 617b1a851d48
Revises: ac56062d7eb9
Create Date: 2023-07-20 13:57:03.931828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '617b1a851d48'
down_revision = 'ac56062d7eb9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('newuser',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('user_id', sa.BigInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('newuser')
