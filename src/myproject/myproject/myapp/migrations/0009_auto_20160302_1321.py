# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20160301_1622'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UndergraduateCourse',
            new_name='UnderOrGraduateCourse',
        ),
        migrations.RenameModel(
            old_name='UndergraduateSection',
            new_name='UnderOrGraduateSection',
        ),
        migrations.RenameField(
            model_name='emphasisarea',
            old_name='numOfCourse',
            new_name='numOfRowToDisplay',
        ),
        migrations.RenameField(
            model_name='emphasisareacourse',
            old_name='isSelected',
            new_name='isRequriedToDispaly',
        ),
        migrations.RenameField(
            model_name='underorgraduatecourse',
            old_name='isSelected',
            new_name='isRequriedToDispaly',
        ),
        migrations.RenameField(
            model_name='underorgraduatesection',
            old_name='numOfCourse',
            new_name='numOfRowToDisplay',
        ),
    ]
