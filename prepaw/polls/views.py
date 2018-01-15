# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index():
    return HttpResponse("Hello, world. You're at the polls index.")


def blah():
    return HttpResponse("Hello, blah-blah.")
