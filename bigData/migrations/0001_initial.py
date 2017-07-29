# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=24)),
                ('content_template', models.CharField(max_length=60)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=1, to='bigData.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tile_Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Tile', max_length=24)),
                ('time', models.DateTimeField(verbose_name=b'refresh time')),
                ('data', jsonfield.fields.JSONField(default={})),
                ('url', models.CharField(default=b'gov.data.au', max_length=260)),
            ],
        ),
        migrations.CreateModel(
            name='Tile_tileData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataId', models.ForeignKey(to='bigData.Tile_Data')),
                ('tileId', models.ForeignKey(to='bigData.Tile')),
            ],
        ),
    ]
