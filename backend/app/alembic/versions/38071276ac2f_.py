"""empty message

Revision ID: 38071276ac2f
Revises: 
Create Date: 2023-08-11 00:54:57.342928

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "38071276ac2f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "portfolio_ticker",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("portfolio_id", sa.Integer(), nullable=True),
        sa.Column("ticker_id", sa.Integer(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["portfolio_id"],
            ["portfolio.id"],
        ),
        sa.ForeignKeyConstraint(
            ["ticker_id"],
            ["ticker.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_portfolio_ticker_id"), "portfolio_ticker", ["id"], unique=False
    )
    op.create_table(
        "transaction",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("ticker_id", sa.Integer(), nullable=True),
        sa.Column("uuid", sa.String(), nullable=True),
        sa.Column("order_type", sa.String(length=10), nullable=True),
        sa.Column("side", sa.String(length=10), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("quantity", sa.Float(), nullable=False),
        sa.Column("fee", sa.Float(), nullable=True),
        sa.Column("status", sa.String(length=10), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["ticker_id"],
            ["ticker.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_transaction_id"), "transaction", ["id"], unique=False)
    op.drop_index("ix_strategy_id", table_name="strategy")
    op.drop_index("ix_simple_transaction_id", table_name="simple_transaction")
    op.drop_table("simple_transaction")
    op.drop_table("portfolio_memo")
    op.drop_index("ix_portfolio_transaction_id", table_name="portfolio_transaction")
    op.drop_table("portfolio_transaction")
    op.drop_index("ix_portfolio_order_id", table_name="portfolio_order")
    op.drop_table("portfolio_order")
    op.add_column("portfolio", sa.Column("is_running", sa.Boolean(), nullable=False))
    op.add_column("portfolio", sa.Column("amount", sa.Integer(), nullable=False))
    op.add_column("portfolio", sa.Column("memo", sa.Text(), nullable=True))
    op.add_column("portfolio", sa.Column("rebal_dt", sa.Date(), nullable=True))
    op.drop_constraint("portfolio_ticker_id_fkey", "portfolio", type_="foreignkey")
    op.drop_column("portfolio", "ticker_id")
    op.drop_column("portfolio", "weight")
    op.drop_table("strategy")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "portfolio",
        sa.Column("weight", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "portfolio",
        sa.Column("ticker_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "portfolio_ticker_id_fkey", "portfolio", "ticker", ["ticker_id"], ["id"]
    )
    op.drop_column("portfolio", "rebal_dt")
    op.drop_column("portfolio", "memo")
    op.drop_column("portfolio", "amount")
    op.drop_column("portfolio", "is_running")
    op.create_table(
        "portfolio_order",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('portfolio_order_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("portfolio_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("strategy_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("is_running", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("amount", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["portfolio_id"], ["portfolio.id"], name="portfolio_order_portfolio_id_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["strategy_id"], ["strategy.id"], name="portfolio_order_strategy_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="portfolio_order_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_portfolio_order_id", "portfolio_order", ["id"], unique=False)
    op.create_table(
        "portfolio_transaction",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "portfolio_order_id", sa.INTEGER(), autoincrement=False, nullable=True
        ),
        sa.Column("uuid", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("ticker_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column(
            "order_type", sa.VARCHAR(length=10), autoincrement=False, nullable=True
        ),
        sa.Column("side", sa.VARCHAR(length=10), autoincrement=False, nullable=False),
        sa.Column(
            "price",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "quantity",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "fee", sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True
        ),
        sa.Column("is_fiiled", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["portfolio_order_id"],
            ["portfolio_order.id"],
            name="portfolio_transaction_portfolio_order_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["ticker_id"], ["ticker.id"], name="portfolio_transaction_ticker_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="portfolio_transaction_pkey"),
    )
    op.create_index(
        "ix_portfolio_transaction_id", "portfolio_transaction", ["id"], unique=False
    )
    op.create_table(
        "portfolio_memo",
        sa.Column("portfolio_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("content", sa.TEXT(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["portfolio_id"], ["portfolio.id"], name="portfolio_memo_portfolio_id_fkey"
        ),
        sa.PrimaryKeyConstraint("portfolio_id", name="portfolio_memo_pkey"),
    )
    op.create_table(
        "simple_transaction",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("ticker_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("uuid", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column(
            "order_type", sa.VARCHAR(length=10), autoincrement=False, nullable=True
        ),
        sa.Column("side", sa.VARCHAR(length=10), autoincrement=False, nullable=False),
        sa.Column(
            "price",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "quantity",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "fee", sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True
        ),
        sa.Column("status", sa.VARCHAR(length=10), autoincrement=False, nullable=True),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["ticker_id"], ["ticker.id"], name="simple_transaction_ticker_id_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name="simple_transaction_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="simple_transaction_pkey"),
    )
    op.create_index(
        "ix_simple_transaction_id", "simple_transaction", ["id"], unique=False
    )
    op.create_table(
        "strategy",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "strategy_nm", sa.VARCHAR(length=20), autoincrement=False, nullable=False
        ),
        sa.Column(
            "strategy_knm", sa.VARCHAR(length=20), autoincrement=False, nullable=False
        ),
        sa.Column("strategy_desc", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.PrimaryKeyConstraint("id", name="strategy_pkey"),
        sa.UniqueConstraint("strategy_knm", name="strategy_strategy_knm_key"),
        sa.UniqueConstraint("strategy_nm", name="strategy_strategy_nm_key"),
    )
    op.create_index("ix_strategy_id", "strategy", ["id"], unique=False)
    op.drop_index(op.f("ix_transaction_id"), table_name="transaction")
    op.drop_table("transaction")
    op.drop_index(op.f("ix_portfolio_ticker_id"), table_name="portfolio_ticker")
    op.drop_table("portfolio_ticker")
    # ### end Alembic commands ###