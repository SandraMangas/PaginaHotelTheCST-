"""
create table reserva
date created: 2021-10-29 06:51:02.496878
"""


def upgrade(migrator):
    with migrator.create_table('reserva') as table:
        table.primary_key('id')
        table.foreign_key('TEXT', 'habitacion_id', on_delete=None, on_update=None, references='habitacion.id')
        table.text('usuario')
        table.text('nombre_cliente')
        table.text('apellido_cliente')
        table.text('telefono_cliente')
        table.text('email_cliente')
        table.text('direccion_cliente')
        table.date('fecha_ingreso')
        table.date('fecha_salida')
        table.int('cant_personas')
        table.int('estado')


def downgrade(migrator):
    migrator.drop_table('reserva')
