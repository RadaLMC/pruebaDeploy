# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_de_serie', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=125)),
                ('descripcion', models.CharField(max_length=125)),
                ('precio_unitario', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
