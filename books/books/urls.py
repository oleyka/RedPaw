from django.conf.urls import include, url
from django.contrib import admin
from studbooks import views

urlpatterns = [
    url(r'^dogs/$', views.list_dogs),
    url(r'^admin/', include(admin.site.urls)),
]
