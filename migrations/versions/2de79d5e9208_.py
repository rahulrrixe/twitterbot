"""empty message

Revision ID: 2de79d5e9208
Revises: None
Create Date: 2014-10-05 05:11:31.978727

"""

# revision identifiers, used by Alembic.
revision = '2de79d5e9208'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('auth_token', sa.String(length=80), nullable=False),
    sa.Column('auth_secret', sa.String(length=80), nullable=False),
    sa.Column('consumer_key', sa.String(length=80), nullable=False),
    sa.Column('consumer_secret', sa.String(length=80), nullable=False),
    sa.Column('job_status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('hashtag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('hostname', sa.String(length=20), nullable=True),
    sa.Column('flagger', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    op.drop_table('hashtag')
    op.drop_table('user')
    ### end Alembic commands ###
