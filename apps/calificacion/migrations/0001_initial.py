# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '__first__'),
        ('materia', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calificacion', models.FloatField()),
                ('alumno', models.ForeignKey(to='alumno.alumno')),
                ('materia', models.ForeignKey(to='materia.materia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
