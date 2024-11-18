"""empty message

Revision ID: 6c39fbae4591
Revises: 
Create Date: 2024-11-18 22:36:53.246992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c39fbae4591'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Ensure no NULL values exist in the column
    op.execute(
        "UPDATE user_profiles SET last_active = CURRENT_TIMESTAMP WHERE last_active IS NULL"
    )
    # Apply the NOT NULL constraint
    with op.batch_alter_table('user_profiles') as batch_op:
        batch_op.alter_column('last_active', nullable=False)

def downgrade():
    with op.batch_alter_table('user_profiles') as batch_op:
        batch_op.alter_column('last_active', nullable=True)