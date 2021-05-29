"""empty message

Revision ID: bf06040f0564
Revises: 
Create Date: 2021-05-29 15:56:55.192288

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'bf06040f0564'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hoges',
                    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(
                        binary=False), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('state', sa.String(length=255), nullable=False),
                    sa.Column('createTime', sa.DateTime(), nullable=False),
                    sa.Column('updateTime', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hoges')
    # ### end Alembic commands ###