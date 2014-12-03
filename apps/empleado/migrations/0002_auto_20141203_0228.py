# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(default=datetime.datetime(2014, 12, 3, 2, 27, 16, 370773, tzinfo=utc), upload_to=b'/foto/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='empleado',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='localidad',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='municipio',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='perfil',
            field=models.ForeignKey(blank=True, to='perfil.perfil', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='sexo',
            field=models.CharField(default=datetime.datetime(2014, 12, 3, 2, 28, 7, 154379, tzinfo=utc), max_length=100, choices=[(b'Hombre', b'Hombre'), (b'Mujer', b'Mujer')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
