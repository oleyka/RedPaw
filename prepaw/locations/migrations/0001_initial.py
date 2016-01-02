# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('animal', models.CharField(max_length=20, choices=[(b'cat', b'cat'), (b'dog', b'dog'), (b'horse', b'horse'), (b'barnyard', b'barnyard'), (b'bird', b'bird'), (b'rabbit', b'rabbit')])),
                ('gender', models.CharField(default=b'unknown', max_length=1, choices=[(b'F', b'female'), (b'M', b'male'), (b'U', b'unknown')])),
                ('neuter', models.CharField(default=b'unknown', max_length=1, choices=[(b'I', b'intact'), (b'N', b'neutered'), (b'U', b'unknown')])),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('age', models.CharField(max_length=200, null=True, blank=True)),
                ('size', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
                ('markings', models.CharField(max_length=200, null=True, blank=True)),
                ('breed', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('intake_date', models.DateTimeField(null=True, verbose_name=b'intake date', blank=True)),
                ('intake_info', models.CharField(blank=True, max_length=20, null=True, choices=[(b'transfer', b'transfer'), (b'owner', b'owner'), (b'sar/authorities', b'sar/authorities'), (b'individual', b'individual')])),
                ('discharge_date', models.DateTimeField(null=True, verbose_name=b'discharge date', blank=True)),
                ('discharge_info', models.CharField(blank=True, max_length=20, null=True, choices=[(b'transfer', b'transfer'), (b'adoption', b'adoption'), (b'deceased', b'deceased'), (b'owner', b'owner')])),
                ('animal_id', models.CharField(max_length=100, null=True, verbose_name=b'crate number or other id', blank=True)),
                ('foster', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('phone', models.CharField(max_length=200, null=True, blank=True)),
                ('hours', models.CharField(max_length=200, null=True, blank=True)),
                ('info', models.CharField(max_length=2000, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='intake',
            name='location',
            field=models.ForeignKey(to='locations.Location'),
        ),
        migrations.AddField(
            model_name='animal',
            name='locations',
            field=models.ManyToManyField(to='locations.Intake'),
        ),
    ]
