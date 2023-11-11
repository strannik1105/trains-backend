"""Add wagon model

Revision ID: e229530e2fe6
Revises: 257bd4961d23
Create Date: 2023-11-11 18:35:53.888099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e229530e2fe6"
down_revision = "257bd4961d23"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA wagons")
    op.create_table(
        "wagon",
        sa.Column("sid", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("wagon_st_disl_sid", sa.Integer(), nullable=True),
        sa.Column("wagon_st_dest_sid", sa.Integer(), nullable=True),
        sa.Column("train_sid", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["train_sid"],
            ["trains.train.sid"],
        ),
        sa.ForeignKeyConstraint(
            ["wagon_st_dest_sid"],
            ["stations.station.sid"],
        ),
        sa.ForeignKeyConstraint(
            ["wagon_st_disl_sid"],
            ["stations.station.sid"],
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="wagons",
        comment="Table with all wagons",
    )
    op.create_index(
        op.f("ix_wagons_wagon_sid"), "wagon", ["sid"], unique=True, schema="wagons"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_wagons_wagon_sid"), table_name="wagon", schema="wagons")

    op.drop_table("wagon", schema="wagons")
    op.execute("DROP SCHEMA wagons")
    # ### end Alembic commands ###
