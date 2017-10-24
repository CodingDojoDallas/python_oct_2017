from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^session_words$', views.index),
    url(r'^add_word$', views.create),
    url(r'^clear_session$', views.clear),
]
