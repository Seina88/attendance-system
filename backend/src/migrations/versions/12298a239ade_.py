"""empty message

Revision ID: 12298a239ade
Revises: 
Create Date: 2021-06-10 21:52:23.183748

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '12298a239ade'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), nullable=False),
                    sa.Column('nickname', sa.String(
                        length=255), nullable=False),
                    sa.Column('first_name', sa.String(
                        length=255), nullable=False),
                    sa.Column('last_name', sa.String(
                        length=255), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('password', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('nickname')
                    )
    op.create_table('sessions',
                    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), nullable=False),
                    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), nullable=False),
                    sa.Column('api_token', sa.String(
                        length=255), nullable=False),
                    sa.Column('expire_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('api_token')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sessions')
    op.drop_table('users')
    # ### end Alembic commands ###
