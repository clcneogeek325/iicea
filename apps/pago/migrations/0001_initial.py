# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
        ('concepto_pago', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('cantidad', models.FloatField()),
                ('alumno', models.ForeignKey(to='alumno.alumno')),
                ('concepto_pago', models.ForeignKey(to='concepto_pago.concepto_pago')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
