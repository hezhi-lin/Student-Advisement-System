# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20160302_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emphasisareacourse',
            old_name='isRequriedToDispaly',
            new_name='isRequiredToDispaly',
        ),
        migrations.RenameField(
            model_name='underorgraduatecourse',
            old_name='isRequriedToDispaly',
            new_name='isRequiredToDispaly',
        ),
    ]
