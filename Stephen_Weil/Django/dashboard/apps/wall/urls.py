from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<userid>\d+)/post', views.post),
    url(r'^/(?P<userid>\d+)/(?P<postid>\d+)/reply', views.reply),
    url(r'^/(?P<userid>\d+)', views.index),
]