"""
create table calificacion
date created: 2021-10-21 02:07:22.586902
"""


def upgrade(migrator):
    with migrator.create_table('calificacion') as table:
        table.primary_key('id')
        table.foreign_key('AUTO', 'habitacion_id', on_delete=None, on_update=None, references='habitacion.id')
        table.foreign_key('TEXT', 'cliente_id', on_delete=None, on_update=None, references='cliente.usuario_id')
        table.text('comentario')
        table.int('calificacion')


def downgrade(migrator):
    migrator.drop_table('calificacion')
