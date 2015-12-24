from django.contrib import admin

from .models import Location, Intake, Animal


class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Animal', { 'fields': ['animal', 'breed', 'gender', 'neuter', 'age', 'size', 'color', 'markings'] }),
        ('History', { 'fields': ['history'] }),
    ]


admin.site.register(Location)
admin.site.register(Animal)
