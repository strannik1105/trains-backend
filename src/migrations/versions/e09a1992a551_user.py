"""User

Revision ID: e09a1992a551
Revises: 
Create Date: 2023-11-02 01:12:47.143398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e09a1992a551"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA users")
    op.create_table(
        "user",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "role", sa.Enum("SUPERUSER", "ADMIN", "MEMBER", name="role"), nullable=True
        ),
        sa.Column("sid", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("sid"),
        schema="users",
        comment="Table with all users",
    )
    op.create_index(
        op.f("ix_users_user_sid"), "user", ["sid"], unique=True, schema="users"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_user_sid"), table_name="user", schema="users")
    op.drop_table("user", schema="users")
    op.execute("DROP TYPE role")
    op.execute("DROP SCHEMA users")
    # ### end Alembic commands ###