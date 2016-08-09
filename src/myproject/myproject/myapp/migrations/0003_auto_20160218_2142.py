# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160218_1909'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='undergraduate',
            unique_together=set([('courseId', 'version', 'section')]),
        ),
    ]
