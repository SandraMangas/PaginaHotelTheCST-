"""
create table reserva
date created: 2021-10-27 20:55:39.205743
"""


def upgrade(migrator):
    with migrator.create_table('reserva') as table:
        table.primary_key('id')
        table.foreign_key('AUTO', 'habitacion_id', on_delete=None, on_update=None, references='habitacion.id')
        table.foreign_key('TEXT', 'usuario_id', on_delete=None, on_update=None, references='usuario.username')
        table.date('fecha_ingreso')
        table.date('fecha_salida')
        table.int('cant_personas')
        table.int('deleted')


def downgrade(migrator):
    migrator.drop_table('reserva')
