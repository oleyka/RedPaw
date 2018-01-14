from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blah', views.blah, name='blah'),
]
