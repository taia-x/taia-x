"""init

Revision ID: 7043ce8dd268
Revises: 
Create Date: 2022-01-17 01:26:02.393018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7043ce8dd268'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'nftdata',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nft_id', sa.Integer, nullable=True),
        sa.Column('data_filename', sa.String, nullable=False),
        sa.Column('path_to_data', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('nftdata')
