from django.conf.urls import url, include # Make Sure to add INCLUDE !
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('apps.semi_restful_app.urls')), # This will link to your app urls
    url(r'^users/', include('apps.semi_restful_app.urls')), # This will link to your app urls
]
