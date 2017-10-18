from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'courses/add', views.add),
    url(r'courses/destroy/(?P<courseid>\d+)', views.destroy),
    url(r'courses/delete/(?P<courseid>\d+)', views.delete),
    url(r'^', views.index)
]