from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<num>\d+)/delete$', views.destroy),
    url(r'^(?P<num>\d+)/edit$', views.edit),
    url(r'^(?P<num>\d+)$', views.show),
    url(r'^new$', views.new),
    url(r'^blogs/create$', views.create),
    url(r'^$', views.index)
]
