# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.CharField(max_length=20, null=True)),
                ('curp', models.CharField(max_length=20, null=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('localidad', models.CharField(max_length=30, null=True)),
                ('municipio', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('dia', models.CharField(max_length=20, null=True)),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('alumno', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
