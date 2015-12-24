from django.contrib import admin

from .models import Location, Intake, Animal


class AnimalHistory(admin.StackedInline):
    model = Intake
    extra = 3


class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Animal', { 'fields': ['animal', 'breed', 'gender', 'neuter', 'age', 'size', 'color', 'markings'] }),
    ]
    inlines = [AnimalHistory]


admin.site.register(Location)
admin.site.register(Animal, AnimalAdmin)
