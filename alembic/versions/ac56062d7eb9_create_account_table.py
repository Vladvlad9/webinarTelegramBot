"""create account table

Revision ID: ac56062d7eb9
Revises: 
Create Date: 2023-06-02 15:44:48.571172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac56062d7eb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('user_id', sa.BigInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('courses',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('name', sa.Text(), nullable=False),
                    sa.Column('description', sa.Text(), nullable=False),
                    sa.Column('KeywordsOne', sa.Text()),
                    sa.Column('KeywordsTwo', sa.Text()),
                    sa.Column('KeywordsThree', sa.Text()),
                    sa.Column('date_course', sa.TIMESTAMP()),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('courses')
