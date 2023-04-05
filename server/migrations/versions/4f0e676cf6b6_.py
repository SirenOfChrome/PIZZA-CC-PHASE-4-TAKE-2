"""empty message

Revision ID: 4f0e676cf6b6
Revises: 9bf1ac42e88c
Create Date: 2023-03-29 19:35:25.700383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f0e676cf6b6'
down_revision = '9bf1ac42e88c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               nullable=True)
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###