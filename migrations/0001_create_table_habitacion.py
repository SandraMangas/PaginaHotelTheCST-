"""
create table habitacion
date created: 2021-10-27 20:55:39.197770
"""


def upgrade(migrator):
    with migrator.create_table('habitacion') as table:
        table.primary_key('id')
        table.float('precio')
        table.int('tipo_habitacion')
        table.int('cant_personas')
        table.int('estado')
        table.int('deleted')


def downgrade(migrator):
    migrator.drop_table('habitacion')
