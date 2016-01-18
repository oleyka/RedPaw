from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_locations, name='list_locations'),
    url(r'^animals/$', views.list_animals, name='list_animals'),
    url(r'^dogs/$', views.list_animals, name='list_animals'),
    url(r'^cats/$', views.list_animals, name='list_animals'),
]
