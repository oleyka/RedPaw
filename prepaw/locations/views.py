from django.shortcuts import render

from .models import Location, Animal


def list_locations(request):
    locations = Location.objects.filter()
    context = { 'locations': locations }
    return render(request, 'locations.html', context)


def list_animals(request):
    animals = Animal.objects.filter()
    context = { 'animals': animals }
    return render(request, 'animals.html', context)

