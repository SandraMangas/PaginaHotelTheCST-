"""
create table usuario
date created: 2021-10-21 19:12:07.767588
"""


def upgrade(migrator):
    with migrator.create_table('usuario') as table:
        table.text('username')
        table.text('password')
        table.text('nombre')
        table.text('apellido')
        table.int('rol')


def downgrade(migrator):
    migrator.drop_table('usuario')
