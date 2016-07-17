from __future__ import unicode_literals

"""
RedPaw models
"""

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # all text fields for now
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    hours = models.CharField(max_length=200, blank=True, null=True)
    info = models.CharField(max_length=2000, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Animal(models.Model):
    ANIMAL_TYPES = (
        ('cat', 'cat'),
        ('dog', 'dog'),
        ('horse', 'horse'),
        ('barnyard', 'barnyard'),
        ('bird', 'bird'),
        ('rabbit', 'rabbit')
    )
    ANIMAL_GENDER = (
        ('F', 'female'),
        ('M', 'male'),
        ('U', 'unknown')
    )
    ANIMAL_NEUTER = (
        ('I', 'intact'),
        ('N', 'neutered'),
        ('U', 'unknown')
    )
    ANIMAL_AGE = (
        ('B', 'baby'),
        ('Y', 'young'),
        ('A', 'adult'),
        ('S', 'senior'),
        ('U', 'unknown'),
    )
    animal = models.CharField(max_length=20, choices=ANIMAL_TYPES)
    gender = models.CharField(max_length=1, default='U', choices=ANIMAL_GENDER)
    neuter = models.CharField(max_length=1, default='U', choices=ANIMAL_NEUTER)
    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=1, default='U', choices=ANIMAL_AGE)
    size = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    markings = models.CharField(max_length=2000, blank=True, null=True)
    breed = models.CharField(max_length=200, blank=True, null=True)
    # where the animal came from
    town = models.CharField(max_length=100, blank=True, null=True)
    locality = models.CharField(max_length=100, blank=True, null=True)

    def history(self):
        return Intake.objects.filter(animal=self.id).all()

    def __unicode__(self):
        return self.animal + ' (id = ' + str(self.id) + ')'


class Intake(models.Model):
    RECEIVED_FROM = (
        ('transfer', 'transfer'),
        ('owner', 'owner'),
        ('sar/authorities', 'sar/authorities'),
        ('individual', 'individual')
    )
    DISCHARGED_TO = (
        ('transfer', 'transfer'),
        ('adoption', 'adoption'),
        ('deceased', 'deceased'),
        ('owner', 'owner')
    )
    location = models.ForeignKey(Location)
    animal = models.ForeignKey(Animal)
    tag = models.CharField('crate number or other id', max_length=100, blank=True, null=True)
    intake_date = models.DateTimeField('intake date', blank=True, null=True)
    intake_info = models.CharField(
        max_length=20,
        choices=RECEIVED_FROM,
        blank=True, null=True
    )
    discharge_date = models.DateTimeField('discharge date', blank=True, null=True)
    discharge_info = models.CharField(
        max_length=20,
        choices=DISCHARGED_TO,
        blank=True, null=True
    )
    foster = models.BooleanField(default=False)

    def __unicode__(self):
        return self.location.name + ': ' + self.animal.animal
