# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='asistencia_empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('fecha', models.DateField()),
                ('activo', models.BooleanField(default=True)),
                ('empleados', models.ManyToManyField(to='empleado.empleado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
