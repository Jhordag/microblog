"""add language to posts

Revision ID: d13d7ff31b47
Revises: bee4a8a30cd3
Create Date: 2022-02-04 14:41:47.752408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd13d7ff31b47'
down_revision = 'bee4a8a30cd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
