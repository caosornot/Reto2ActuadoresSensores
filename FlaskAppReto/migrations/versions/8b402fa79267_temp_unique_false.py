"""Temp unique=False

Revision ID: 8b402fa79267
Revises: 8eb0368d4037
Create Date: 2018-04-09 01:42:31.397120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b402fa79267'
down_revision = '8eb0368d4037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_reg_temp_temp', table_name='reg_temp')
    op.create_index(op.f('ix_reg_temp_temp'), 'reg_temp', ['temp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reg_temp_temp'), table_name='reg_temp')
    op.create_index('ix_reg_temp_temp', 'reg_temp', ['temp'], unique=1)
    # ### end Alembic commands ###
