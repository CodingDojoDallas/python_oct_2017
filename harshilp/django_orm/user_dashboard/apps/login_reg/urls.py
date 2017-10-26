from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),    
    url(r'^loginProcess$', views.loginProcess),
    url(r'^registerProcess$', views.registerProcess)
]

