from django.urls import path
from django.urls import re_path as url
from .import views

app_name='landing'

urlpatterns=[
    path('', views.index, name="index"),
    ]
