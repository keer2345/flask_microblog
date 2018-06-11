"""empty message

Revision ID: 94538f7310b5
Revises: 63169609d517
Create Date: 2018-06-11 12:00:11.225911

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '94538f7310b5'
down_revision = '63169609d517'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_table('user')
    op.drop_constraint('followers_follower_id_fkey', 'followers', type_='foreignkey')
    op.drop_constraint('followers_followed_id_fkey', 'followers', type_='foreignkey')
    op.create_foreign_key(None, 'followers', 'users', ['followed_id'], ['id'])
    op.create_foreign_key(None, 'followers', 'users', ['follower_id'], ['id'])
    op.drop_constraint('post_user_id_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_user_id_fkey', 'post', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'followers', type_='foreignkey')
    op.drop_constraint(None, 'followers', type_='foreignkey')
    op.create_foreign_key('followers_followed_id_fkey', 'followers', 'user', ['followed_id'], ['id'])
    op.create_foreign_key('followers_follower_id_fkey', 'followers', 'user', ['follower_id'], ['id'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('about_me', sa.VARCHAR(length=140), autoincrement=False, nullable=True),
    sa.Column('last_seen', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
