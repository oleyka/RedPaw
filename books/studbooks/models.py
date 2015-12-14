from django.db import models

# Pedigree and Canine models have to take into account the discrepancies
# that are present in the databases used to feed the data

class Canine(models.Model):
    # most common name in Engish
    name = models.CharField(max_length=200)
    # alternative names (combined from the pedigrees)
    alt_name = models.CharField(max_length=2000, blank=True, null=True)

    def __init__(self):
        # these duplicate the pedigree data
        # TODO add logic for best version if there are discrepancies
        self.pedigrees = models.ManyToManyField(Pedigree, blank=True, null=True)
        self.sire = models.ForeignKey(Canine, blank=True, null=True, on_delete=models.CASCADE)
        self.dam = models.ForeignKey(Canine, blank=True, null=True, on_delete=models.CASCADE)
        self.birth_date = models.birth_date = models.DateField(blank=True, null=True)
        self.breed = models.CharField(max_length=60, blank=True, null=True)
        self.color = models.CharField(max_length=60, blank=True, null=True)
        self.gender = models.ManyToManyField(Pedigree, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Pedigree(models.Model):
    # data as recorded in the pedigree, even if incorrect
    # TODO split into meaningful parts as per registry's format
    number = models.CharField(max_length=60, primary_key=True)
    # TODO enum
    registry = models.CharField(max_length=60, blank=True, null=True)
    # name as written in the pedigree
    name = models.CharField(max_length=200, blank=True, null=True)
    # name in alternative language (English or vice versa)
    translit_name = models.CharField(max_length=200, blank=True, null=True)
    # alternative spelling (e.g. different source)
    alt_name = models.CharField(max_length=200, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    breed = models.CharField(max_length=60, blank=True, null=True)
    # TODO enum
    color = models.CharField(max_length=60, blank=True, null=True)
    gender = models.BooleanField()
    sire = models.ForeignKey(Canine, blank=True, null=True, on_delete=models.CASCADE, related_name='sire')
    dam = models.ForeignKey(Canine, blank=True, null=True, on_delete=models.CASCADE, related_name='dam')

    def __unicode__(self):
        return self.number
