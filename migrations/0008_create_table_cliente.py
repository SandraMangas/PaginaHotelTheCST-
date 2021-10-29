"""
create table cliente
date created: 2021-10-29 05:40:20.492643
"""


def upgrade(migrator):
    with migrator.create_table('cliente') as table:
        table.foreign_key('TEXT', 'usuario_id', on_delete=None, on_update=None, references='usuario.username')
        table.text('telefono')
        table.text('email')
        table.text('direccion')


def downgrade(migrator):
    migrator.drop_table('cliente')
