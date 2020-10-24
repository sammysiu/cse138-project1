# Code taken from django projects intro tutorial

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<name>', views.names, name='names'),
]
