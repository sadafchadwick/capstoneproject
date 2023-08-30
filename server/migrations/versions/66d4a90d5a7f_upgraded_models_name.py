"""upgraded models name

Revision ID: 66d4a90d5a7f
Revises: ed433963aa4a
Create Date: 2023-08-29 20:38:13.835436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66d4a90d5a7f'
down_revision = 'ed433963aa4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventoryitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_inventoryitems_item_id_items')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_inventoryitems_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('inventories')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventories',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('quantity', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('item_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name='fk_inventories_item_id_items'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_inventories_user_id_users'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('inventoryitems')
    # ### end Alembic commands ###
