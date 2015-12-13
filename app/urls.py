from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dogs/$', views.list_dogs),
]
