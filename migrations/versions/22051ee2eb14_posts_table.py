"""posts table

Revision ID: 22051ee2eb14
Revises: 2b122f2e67ef
Create Date: 2022-01-30 17:21:07.578224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22051ee2eb14'
down_revision = '2b122f2e67ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
