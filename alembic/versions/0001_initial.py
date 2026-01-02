"""initial migration - マスターデータと

Revision ID: 0001_initial
Revises: 
Create Date: 2026-01-02
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None
    
def upgrade():
    op.create_table(
        'mst_users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('user', sa.String(length=100), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )
    op.create_table(
        'mst_kaji',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('kaji', sa.String(length=100), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )
    op.create_table(
        'tbl_kaji',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('kaji_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('done_date', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        # 外部キー制約
        sa.ForeignKeyConstraint(['kaji_id'], ['mst_kaji.id']),
        sa.ForeignKeyConstraint(['user_id'], ['mst_users.id']),
    )


def downgrade():
    op.drop_table('tbl_kaji')#削除順番を考慮する
    op.drop_table('mst_kaji')
    op.drop_table('mst_users')
sa.Column('created_at', sa.DateTime(), nullable=True),
sa.Column('updated_at', sa.DateTime(), nullable=True),