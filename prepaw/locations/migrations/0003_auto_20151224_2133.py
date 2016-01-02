# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20151224_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='locations',
            new_name='history',
        ),
    ]
