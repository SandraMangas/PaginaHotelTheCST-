"""
create table habitacion
date created: 2021-10-29 05:40:20.488671
"""


def upgrade(migrator):
    with migrator.create_table('habitacion') as table:
        table.text('id')
        table.float('precio')
        table.int('tipo_habitacion')
        table.int('cant_personas')
        table.int('estado')
        table.int('deleted')


def downgrade(migrator):
    migrator.drop_table('habitacion')
