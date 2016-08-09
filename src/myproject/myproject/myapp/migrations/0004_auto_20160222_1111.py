# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160218_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='UndergraduateCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseId', models.CharField(max_length=255)),
                ('courseTitle', models.CharField(max_length=255)),
                ('isSelected', models.BooleanField(default=True)),
                ('creditHour', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UndergraduateSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('program', models.CharField(max_length=255)),
                ('sectionId', models.IntegerField()),
                ('sectionTitle', models.CharField(max_length=255)),
                ('numOfCourse', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Undergraduate',
        ),
        migrations.AlterUniqueTogether(
            name='undergraduatesection',
            unique_together=set([('program', 'sectionId')]),
        ),
        migrations.AddField(
            model_name='undergraduatecourse',
            name='section',
            field=models.ForeignKey(to='myapp.UndergraduateSection'),
        ),
        migrations.AlterUniqueTogether(
            name='undergraduatecourse',
            unique_together=set([('courseId', 'section')]),
        ),
    ]
