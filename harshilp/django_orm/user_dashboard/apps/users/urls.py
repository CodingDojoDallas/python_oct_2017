from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^new$', views.new),
    url(r'^edit$', views.edit),
    url(r'^editProfile$', views.editProfile),      
    url(r'^show/(?P<user_id>\d+)$', views.show), 
    url(r'^edit/(?P<user_id>\d+)$', views.editAdmin),
    url(r'^post/(?P<user_id>\d+)$', views.post),
    url(r'^comment/(?P<user_id>\d+)/(?P<message_id>\d+)$', views.comment),
    url(r'^logoff', views.logoff)
    
]