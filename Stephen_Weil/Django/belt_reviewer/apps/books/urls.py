from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/add', views.addpage),
    url(r'^/create', views.create),
    url(r'^/show/(?P<bookid>\d+)', views.bookpage),
    url(r'^/(?P<bookid>\d+)/reviews/add', views.review),
    url(r'^/review/delete/(?P<reviewid>\d+)', views.delete)
]