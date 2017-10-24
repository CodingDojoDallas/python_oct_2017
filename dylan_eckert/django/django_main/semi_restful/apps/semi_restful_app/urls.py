from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="all_users"),
#This has a name of "all_users", which means it is a named route!
#This points to views.INDEX in your views.py // its used in the new.html
    url(r'^new$', views.new, name="new_user"),
# Now we need a NEW METHOD in the views.py
    url(r'^create$', views.create, name="create_user"),
#Any url must be defined in the views.py  => Define create in the views.py
    url(r'^show/(?P<id>\d+)$', views.show, name="show_user"),
#Now you need a show method in views.py
]
