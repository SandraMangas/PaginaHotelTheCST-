"""
create table usuario
date created: 2021-10-27 20:55:39.199758
"""


def upgrade(migrator):
    with migrator.create_table('usuario') as table:
        table.text('username')
        table.text('password')
        table.text('nombre')
        table.text('apellido')
        table.int('tipo_usuario')
        table.int('deleted')


def downgrade(migrator):
    migrator.drop_table('usuario')
