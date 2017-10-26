from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/(?P<userid>\d+)/edit', views.edit),
    url(r'^users/(?P<userid>\d+)/delete', views.delete),
    url(r'^users/(?P<userid>\d+)/update', views.update),
    url(r'^users/(?P<userid>\d+)', views.show),
    url(r'^users/add', views.add),
    url(r'^users/create', views.create),
    url(r'^', views.index)
]