from django.contrib import admin

from .models import Location, Intake, Animal


class AnimalHistory(admin.TabularInline):
    model = Intake
    extra = 1


class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Animal', { 'fields': ['animal', 'breed', 'gender', 'neuter', 'age', 'size', 'color', 'markings'] }),
    ]
    inlines = [AnimalHistory]
    list_display = ('animal', 'breed', 'gender', 'color', 'locality')
    list_filter = ['animal', 'gender', 'breed', 'color', 'age', 'locality']
    search_fields = ['locality', 'town']


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'hours')


admin.site.register(Location, LocationAdmin)
admin.site.register(Animal, AnimalAdmin)
