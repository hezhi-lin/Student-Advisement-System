# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20160302_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='underorgraduatecourse',
            name='creditHour',
            field=models.IntegerField(default=3),
        ),
    ]
