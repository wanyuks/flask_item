"""empty message

Revision ID: d3ef967d7741
Revises: 
Create Date: 2019-12-11 21:13:05.808883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3ef967d7741'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('s_id', sa.Integer(), nullable=False),
    sa.Column('s_name', sa.String(length=32), nullable=True),
    sa.Column('_s_password', sa.String(length=256), nullable=True),
    sa.Column('s_phone', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('s_id'),
    sa.UniqueConstraint('s_name'),
    sa.UniqueConstraint('s_phone')
    )
    op.create_table('users_new',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_new')
    op.drop_table('students')
    # ### end Alembic commands ###
