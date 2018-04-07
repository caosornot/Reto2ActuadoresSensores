"""users table

Revision ID: 8d745ae74af7
Revises: 0011ba4a6f10
Create Date: 2018-04-07 17:34:37.404595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d745ae74af7'
down_revision = '0011ba4a6f10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reg_temp', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_reg_temp_timestamp'), 'reg_temp', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reg_temp_timestamp'), table_name='reg_temp')
    op.drop_column('reg_temp', 'timestamp')
    # ### end Alembic commands ###
