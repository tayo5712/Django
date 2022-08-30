from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/asd/', views.hello1, name='hello1'),
    path('hello/<name>/', views.hello, name='hello'),
    
]