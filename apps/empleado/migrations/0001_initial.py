# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('localidad', models.CharField(max_length=30, null=True)),
                ('municipio', models.CharField(max_length=30, null=True)),
                ('telefono', models.CharField(max_length=30, null=True)),
                ('sexo', models.CharField(max_length=30, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('empleado', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('perfil', models.ForeignKey(to='perfil.perfil', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
