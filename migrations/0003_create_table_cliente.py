"""
create table cliente
date created: 2021-10-30 04:07:12.158201
"""


def upgrade(migrator):
    with migrator.create_table('cliente') as table:
        table.foreign_key('TEXT', 'usuario_id', on_delete=None, on_update=None, references='usuario.username')
        table.text('telefono')
        table.text('email')
        table.text('direccion')


def downgrade(migrator):
    migrator.drop_table('cliente')
