"""start migration

Revision ID: 560245253d2a
Revises: 
Create Date: 2022-06-25 17:45:42.711729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '560245253d2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('branch', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='core'
    )
    op.create_index(op.f('ix_core_manager_id'), 'manager', ['id'], unique=True, schema='core')
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='core'
    )
    op.create_index(op.f('ix_core_project_id'), 'project', ['id'], unique=True, schema='core')
    op.create_table('tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_name', sa.String(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['core.project.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='core'
    )
    op.create_index(op.f('ix_core_tables_id'), 'tables', ['id'], unique=True, schema='core')
    op.create_index(op.f('ix_core_tables_table_name'), 'tables', ['table_name'], unique=False, schema='core')
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('row_id', sa.BigInteger(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('manager_id', sa.Integer(), nullable=True),
    sa.Column('new_value', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['core.manager.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['project_id'], ['core.project.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['table_id'], ['core.tables.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='core'
    )
    op.create_index(op.f('ix_core_log_id'), 'log', ['id'], unique=True, schema='core')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_core_log_id'), table_name='log', schema='core')
    op.drop_table('log', schema='core')
    op.drop_index(op.f('ix_core_tables_table_name'), table_name='tables', schema='core')
    op.drop_index(op.f('ix_core_tables_id'), table_name='tables', schema='core')
    op.drop_table('tables', schema='core')
    op.drop_index(op.f('ix_core_project_id'), table_name='project', schema='core')
    op.drop_table('project', schema='core')
    op.drop_index(op.f('ix_core_manager_id'), table_name='manager', schema='core')
    op.drop_table('manager', schema='core')
    # ### end Alembic commands ###
