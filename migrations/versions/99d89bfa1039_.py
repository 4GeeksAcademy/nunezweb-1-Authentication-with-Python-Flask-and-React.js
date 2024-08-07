"""empty message

Revision ID: 99d89bfa1039
Revises: b2367ff2a2c4
Create Date: 2024-07-25 11:46:14.001887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99d89bfa1039'
down_revision = 'b2367ff2a2c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=120), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
