"""create new gg

Revision ID: 47cfc2eaaba8
Revises: 617b1a851d48
Create Date: 2023-07-20 14:04:56.716716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47cfc2eaaba8'
down_revision = '617b1a851d48'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('usersN',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('user_id', sa.BigInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('usersN')
