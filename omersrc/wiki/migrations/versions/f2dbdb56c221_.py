"""empty message

Revision ID: f2dbdb56c221
Revises: 
Create Date: 2017-12-02 15:09:33.156000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2dbdb56c221'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('tag', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('page')
    # ### end Alembic commands ###
