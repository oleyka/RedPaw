# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20151224_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='age',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'B', b'baby'), (b'Y', b'young'), (b'A', b'adult'), (b'S', b'senior'), (b'U', b'unknown')]),
        ),
        migrations.AlterField(
            model_name='animal',
            name='gender',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'F', b'female'), (b'M', b'male'), (b'U', b'unknown')]),
        ),
        migrations.AlterField(
            model_name='animal',
            name='neuter',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'I', b'intact'), (b'N', b'neutered'), (b'U', b'unknown')]),
        ),
    ]
