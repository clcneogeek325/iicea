# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='nomina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField()),
                ('fecha', models.DateTimeField()),
                ('empleado', models.ForeignKey(to='empleado.empleado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
