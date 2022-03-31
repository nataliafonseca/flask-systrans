"""change autos name to vehicles

Revision ID: c4b7d9087210
Revises: 1b0af534e5fe
Create Date: 2022-03-31 12:17:59.708943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4b7d9087210'
down_revision = '1b0af534e5fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('plate', sa.String(), nullable=False),
    sa.Column('car_make', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('year', sa.String(), nullable=False),
    sa.Column('passenger_capacity', sa.String(), nullable=False),
    sa.Column('driver_cpf', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['driver_cpf'], ['people.cpf'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plate')
    )
    op.drop_table('autos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('autos',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.VARCHAR(), nullable=False),
    sa.Column('plate', sa.VARCHAR(), nullable=False),
    sa.Column('car_make', sa.VARCHAR(), nullable=False),
    sa.Column('model', sa.VARCHAR(), nullable=False),
    sa.Column('year', sa.VARCHAR(), nullable=False),
    sa.Column('passenger_capacity', sa.VARCHAR(), nullable=False),
    sa.Column('driver_cpf', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['driver_cpf'], ['people.cpf'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plate')
    )
    op.drop_table('vehicles')
    # ### end Alembic commands ###