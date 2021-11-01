"""
create table usuario
date created: 2021-10-30 04:07:12.156241
"""


def upgrade(migrator):
    with migrator.create_table('usuario') as table:
        table.text('username')
        table.text('password')
        table.text('nombre')
        table.text('apellido')
        table.int('tipo_usuario')
        table.int('estado')
        table.bool('deleted')


def downgrade(migrator):
    migrator.drop_table('usuario')
