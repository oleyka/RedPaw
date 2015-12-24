# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20151224_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intake',
            old_name='animal_id',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='history',
        ),
        migrations.AddField(
            model_name='intake',
            name='animal',
            field=models.ForeignKey(default=1, to='locations.Animal'),
            preserve_default=False,
        ),
    ]
