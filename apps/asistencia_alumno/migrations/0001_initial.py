# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='asistencia_alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('fecha', models.DateField()),
                ('alumno', models.ForeignKey(to='alumno.alumno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
