# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160222_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('programTitle', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='undergraduatesection',
            name='program',
            field=models.ForeignKey(to='myapp.Program'),
        ),
        migrations.AlterUniqueTogether(
            name='program',
            unique_together=set([('programTitle',)]),
        ),
    ]
