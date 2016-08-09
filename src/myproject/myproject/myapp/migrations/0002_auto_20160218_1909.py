# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Undergraduate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseId', models.CharField(max_length=255)),
                ('courseTitle', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('section', models.IntegerField()),
                ('sectionTitle', models.CharField(max_length=255)),
                ('creditHour', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=b'documents'),
        ),
    ]
