# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20160301_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emphasisarea',
            old_name='emphasisAreaIdTitle',
            new_name='emphasisAreaTitle',
        ),
    ]
