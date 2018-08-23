from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    #Login / Register
    path('login/', views.login),
    path('process_login', views.process_login),
    path('register/', views.register),
    path('process_registration', views.process_registration),
    # Trips
    # path('create_trip/', views.create_trip)

]
