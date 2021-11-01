"""
create table habitacion
date created: 2021-10-30 04:07:12.153508
"""


def upgrade(migrator):
    with migrator.create_table('habitacion') as table:
        table.text('id')
        table.float('precio')
        table.int('tipo_habitacion')
        table.int('cant_personas')
        table.int('estado')
        table.bool('deleted')


def downgrade(migrator):
    migrator.drop_table('habitacion')
