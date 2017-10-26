from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signin', views.signin),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^logout', views.logout),
    url(r'^dashboard', views.dashboard),
    url(r'^users/new', views.addpage),
    url(r'^users/create', views.create),
    url(r'^users/edit/(?P<userid>\d+)', views.edit),
    url(r'^users/update/(?P<userid>\d+)', views.update),
    url(r'^', views.index)
]