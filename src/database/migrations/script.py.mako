"""
${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Created At: ${create_date}
"""
from alembic import op
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    op.execute(
        """

        """
    )


def downgrade():
    op.execute(
        """

        """
    )
