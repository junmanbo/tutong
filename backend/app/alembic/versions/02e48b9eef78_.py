"""empty message

Revision ID: 02e48b9eef78
Revises: 264da1fec4ed
Create Date: 2023-07-20 14:18:41.950442

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '02e48b9eef78'
down_revision = '264da1fec4ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_order_type_id', table_name='order_type')
    op.drop_table('order_type')
    op.create_unique_constraint(None, 'exchange_key', ['user_id', 'exchange_id'])
    op.add_column('portfolio_transaction', sa.Column('order_type', sa.String(length=10), nullable=True))
    op.drop_constraint('portfolio_transaction_order_type_id_fkey', 'portfolio_transaction', type_='foreignkey')
    op.drop_column('portfolio_transaction', 'order_type_id')
    op.add_column('simple_transaction', sa.Column('order_type', sa.String(length=10), nullable=True))
    op.alter_column('simple_transaction', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('simple_transaction', 'is_fiiled',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_constraint('simple_transaction_order_type_id_fkey', 'simple_transaction', type_='foreignkey')
    op.drop_column('simple_transaction', 'order_type_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('simple_transaction', sa.Column('order_type_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('simple_transaction_order_type_id_fkey', 'simple_transaction', 'order_type', ['order_type_id'], ['id'])
    op.alter_column('simple_transaction', 'is_fiiled',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('simple_transaction', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('simple_transaction', 'order_type')
    op.add_column('portfolio_transaction', sa.Column('order_type_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('portfolio_transaction_order_type_id_fkey', 'portfolio_transaction', 'order_type', ['order_type_id'], ['id'])
    op.drop_column('portfolio_transaction', 'order_type')
    op.drop_constraint(None, 'exchange_key', type_='unique')
    op.create_table('order_type',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_type_nm', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('order_type_knm', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='order_type_pkey'),
    sa.UniqueConstraint('order_type_knm', name='order_type_order_type_knm_key'),
    sa.UniqueConstraint('order_type_nm', name='order_type_order_type_nm_key')
    )
    op.create_index('ix_order_type_id', 'order_type', ['id'], unique=False)
    # ### end Alembic commands ###