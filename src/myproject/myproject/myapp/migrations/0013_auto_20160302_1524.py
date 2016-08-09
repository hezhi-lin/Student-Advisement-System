# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20160302_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emphasisareacourse',
            name='isRequiredToDispaly',
            field=models.BooleanField(default=False),
        ),
    ]
