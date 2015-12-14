# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studbooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canine',
            name='alt_name',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='alt_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='breed',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='color',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='dam',
            field=models.ForeignKey(related_name='dam', blank=True, to='studbooks.Canine', null=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='registry',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='sire',
            field=models.ForeignKey(related_name='sire', blank=True, to='studbooks.Canine', null=True),
        ),
        migrations.AlterField(
            model_name='pedigree',
            name='translit_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
