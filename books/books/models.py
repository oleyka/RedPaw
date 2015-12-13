from django.db import models

# Pedigree and Canine modelshave to take into account the discrepancies
# that are present in the databases used to feed the data

class Canine(models.Model):
    # most common name in Engish
    name = models.CharField(max_length=200)
    # alternative names (combined from the pedigrees)
    alt_name = models.CharField(max_length=2000, blank=True)
    pedigrees = models.ManyToManyField(Pedigree, blank=True)
    gender = models.BooleanField()

    # these duplicate the pedigree data
    # "official" vesion of there are discrepancies
    birth_date = models.DateField(blank=True)
    breed = models.CharField(max_length=60, blank=True)
    color = models.CharField(max_length=60, blank=True)
    sire = models.ForeignKey(Canine, blank=True, on_delete=models.CASCADE)
    dam = models.ForeignKey(Canine, blank=True, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Pedigree(models.Model):
    # data as recorded in the pedigree, even if incorrect
    # TODO enum
    registry = models.CharField(max_length=60, primary_key=True)
    # TODO split into meaningful parts as per registry's format
    number = models.CharField(max_length=60, primary_key=True)
    # name as written in the pedigree
    name = models.CharField(max_length=200, blank=True)
    # name in alternative language (English or vice versa)
    translit_name = models.CharField(max_length=200, blank=True)
    # alternative spelling (e.g. different source)
    alt_name = models.CharField(max_length=200, blank=True)

    birth_date = models.DateField(blank=True)
    breed = models.CharField(max_length=60, blank=True)
    # TODO enum
    color = models.CharField(max_length=60, blank=True)
    sire = models.ForeignKey(Canine, blank=True, on_delete=models.CASCADE)
    dam = models.ForeignKey(Canine, blank=True, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.number

