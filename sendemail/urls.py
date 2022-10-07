from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url(r'^image_load/$', views.image_load, name='image_load'),
]
