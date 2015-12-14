# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('alt_name', models.CharField(max_length=2000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedigree',
            fields=[
                ('number', models.CharField(max_length=60, serialize=False, primary_key=True)),
                ('registry', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('translit_name', models.CharField(max_length=200, blank=True)),
                ('alt_name', models.CharField(max_length=200, blank=True)),
                ('birth_date', models.DateField(blank=True)),
                ('breed', models.CharField(max_length=60, blank=True)),
                ('color', models.CharField(max_length=60, blank=True)),
                ('gender', models.BooleanField()),
                ('dam', models.ForeignKey(related_name='dam', blank=True, to='studbooks.Canine')),
                ('sire', models.ForeignKey(related_name='sire', blank=True, to='studbooks.Canine')),
            ],
        ),
    ]
