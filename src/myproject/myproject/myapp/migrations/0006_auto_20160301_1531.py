# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20160222_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmphasisArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emphasisAreaId', models.IntegerField()),
                ('emphasisAreaIdTitle', models.CharField(max_length=255)),
                ('numOfCourse', models.IntegerField()),
                ('program', models.ForeignKey(to='myapp.Program')),
            ],
        ),
        migrations.CreateModel(
            name='EmphasisAreaCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseId', models.CharField(max_length=255)),
                ('courseTitle', models.CharField(max_length=255)),
                ('isSelected', models.BooleanField(default=True)),
                ('creditHour', models.IntegerField()),
                ('emphasisArea', models.ForeignKey(to='myapp.EmphasisArea')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='emphasisareacourse',
            unique_together=set([('courseId', 'emphasisArea')]),
        ),
        migrations.AlterUniqueTogether(
            name='emphasisarea',
            unique_together=set([('program', 'emphasisAreaId')]),
        ),
    ]
