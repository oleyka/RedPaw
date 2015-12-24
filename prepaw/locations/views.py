from django.shortcuts import render
from django.http import HttpResponse

from .models import Location, Animal

def list_locations(request):
    locations = Location.objects.filter()
    context = {} ## 'name': name, 'gender': gender }
    return HttpResponse("Listing locations")
#    return render(request, 'templates/locations.html', context)


def list_animals(request):
    animals = Animal.objects.filter()
    context = {} ## 'name': name, 'gender': gender }
    return HttpResponse("Listing animals")
#    return render(request, 'templates/animals.html', context)

