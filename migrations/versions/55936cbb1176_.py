"""empty message

Revision ID: 55936cbb1176
Revises: 6cb5cae4a6b4
Create Date: 2019-11-29 22:43:51.820226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55936cbb1176'
down_revision = '6cb5cae4a6b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topics', schema=None) as batch_op:
        batch_op.drop_constraint('user_foreign_key', type_='foreignkey')
        batch_op.drop_column('close_date')
        batch_op.drop_column('create_uid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_uid', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('close_date', sa.DATETIME(), nullable=True))
        batch_op.create_foreign_key('user_foreign_key', 'users', ['create_uid'], ['id'])

    # ### end Alembic commands ###
