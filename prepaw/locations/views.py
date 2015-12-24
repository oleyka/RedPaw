from django.shortcuts import render

from .models import Location, Animal

def list_locations(request):
    locations = Location.objects.filter()
    context = {} ## 'name': name, 'gender': gender }
    return render(request, 'templates/locations.html', context)


def list_animals(request):
    animals = Animal.objects.filter()
    context = {} ## 'name': name, 'gender': gender }
    return render(request, 'templates/animals.html', context)

