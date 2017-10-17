from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
    url(r'^(?P<building>\w+)$', views.process)
]