"""Add train model

Revision ID: 257bd4961d23
Revises: 39c9cb8c488f
Create Date: 2023-11-11 18:00:04.892488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "257bd4961d23"
down_revision = "39c9cb8c488f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA trains")
    op.create_table(
        "train",
        sa.Column("sid", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("operation_data", sa.Date(), nullable=True),
        sa.Column("train_st_disl_sid", sa.Integer(), nullable=True),
        sa.Column("train_st_dest_sid", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["train_st_dest_sid"],
            ["stations.station.sid"],
        ),
        sa.ForeignKeyConstraint(
            ["train_st_disl_sid"],
            ["stations.station.sid"],
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="trains",
        comment="Table with all trains",
    )
    op.create_index(
        op.f("ix_trains_train_sid"), "train", ["sid"], unique=True, schema="trains"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_trains_train_sid"), table_name="train", schema="trains")

    op.drop_table("train", schema="trains")
    op.execute("DROP SCHEMA trains")
    # ### end Alembic commands ###