"""first migration

Revision ID: d044894abe02
Revises: 
Create Date: 2022-04-11 20:34:25.752055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd044894abe02'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=80), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('salary', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('cashflow', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('tax', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('home_mortgage_payment', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('school_loan_payment', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('car_loan_payment', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('credit_card_payment', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('other_expenses', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('bank_loan_payment', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('children', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('children_expenses', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('savings', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('home_mortgage', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('school_loans', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('car_loans', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('credit_card_debt', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.Column('payday', sa.Numeric(precision=10, scale=0), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    # ### end Alembic commands ###