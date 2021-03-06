"""Added active column to Owner

Revision ID: 2dc72d16c188
Revises: 30d3af507801
Create Date: 2014-03-06 12:02:36.869598

"""

# revision identifiers, used by Alembic.
revision = '2dc72d16c188'
down_revision = '30d3af507801'

from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('owner', sa.Column('active', sa.Boolean(), server_default='True'))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('owner', 'active')
    ### end Alembic commands ###

