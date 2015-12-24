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


class Intake(models.Model):
    RECEIVED_FROM = ( 'transfer', 'owner', 'sar/authorities', 'individual' )
    DISCHARGED_TO = ( 'transfer', 'adoption', 'deceased', 'owner' )
    location = models.ForeignKey(Location)
    intake_date = models.DateTimeField('intake date', blank=True, null=True)
    intake_info = models.CharField(choices=RECEIVED_FROM, blank=True, null=True)
    discharge_date = models.DateTimeField('discharge date', blank=True, null=True)
    discharge_info = models.CharField(choices=DISCHARGED_TO, blank=True, null=True)
    animal_id = models.CharField('crate number or other id', max_length=100, blank=True, null=True)
    foster = models.BooleanField(default=False)

    def __unicode__(self):
        return self.location + ': ' + self.animal_id


class Animal(models.Model):
    ANIMAL_TYPES = ( 'cat', 'dog', 'horse', 'barnyard', 'bird', 'rabbit' )
    ANIMAL_GENDER = ( 'female', 'male', 'unknown' )
    ANIMAL_NEUTER = ( 'intact', 'neutered', 'unknown' )

    locations = models.ManyToManyField(Intake)
    animal = models.CharField(choices=ANIMAL_TYPES)
    gender = models.CharField(default='unknown', choices=ANIMAL_GENDER)
    neuter = models.CharField(default='unknown', choices=ANIMAL_NEUTER)
    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    markings = models.CharField(max_length=200, blank=True, null=True)
    breed = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name + ' (' + self.animal + ')'


