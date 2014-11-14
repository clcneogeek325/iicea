# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concepto_pago', '0001_initial'),
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.FloatField()),
                ('activo', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(to='alumno.alumno')),
                ('concepto_pago', models.ForeignKey(to='concepto_pago.concepto_pago')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
