# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20160301_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='isGraduateProgram',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='emphasisarea',
            name='emphasisAreaId',
            field=models.CharField(max_length=255),
        ),
    ]
