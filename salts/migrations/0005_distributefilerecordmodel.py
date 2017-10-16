# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-16 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salts', '0004_onlinedeploymodel_command'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributeFileRecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=100)),
                ('pattern', models.CharField(max_length=100)),
                ('opttime', models.DateTimeField()),
                ('path', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ops_upload_file_record',
            },
        ),
    ]
