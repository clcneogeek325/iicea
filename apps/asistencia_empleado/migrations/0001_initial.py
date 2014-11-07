# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='asistencia_empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('fecha', models.DateField()),
                ('empleado', models.ForeignKey(to='empleado.empleado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
