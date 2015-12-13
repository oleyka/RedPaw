from django.shortcuts import render

from .models import Canine

def list_dogs(request):
    dogs = Canine.objects.filter()
    context = { 'name': name, 'gender': gender }
    return render(request, 'templates/list.html', context)
