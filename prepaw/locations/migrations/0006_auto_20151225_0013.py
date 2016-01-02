# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20151225_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='locality',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='town',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
