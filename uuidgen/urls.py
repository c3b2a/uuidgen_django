from django.contrib import admin
from django.urls import re_path

from . import views,api,ip

urlpatterns = [
    re_path(r'^$', views.display),
    re_path(r'^api$', api.process),
    re_path(r'^ip$', ip.get_connect_ip)
]
