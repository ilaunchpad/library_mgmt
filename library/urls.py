from django.urls import path
from django.urls import re_path as url
from . import views

app_name = 'library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'books/$',views.books, name='books'),
    #path('', views.index, name='index'),
    #path('books/', views.books, name='books'),
]
