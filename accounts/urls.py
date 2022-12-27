from django.urls import path
from django.urls import re_path as url
from .import views

app_name='accounts'

urlpatterns=[
    path('', views.index, name="index"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    ]
