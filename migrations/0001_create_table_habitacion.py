"""
create table habitacion
date created: 2021-10-21 02:07:22.582186
"""


def upgrade(migrator):
    with migrator.create_table('habitacion') as table:
        table.primary_key('id')
        table.float('precio')
        table.int('cant_personas')
        table.bool('disponible')


def downgrade(migrator):
    migrator.drop_table('habitacion')