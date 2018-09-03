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
    # Logout
    path('logout/', views.logout),
    # Dashboard
    path('dashboard', views.dashboard),
    # Trips
    path('create_trip/', views.create_trip),
    path('process_create_trip', views.process_create_trip),
    path('join_trip/<int:post_id >', views.join_trip),
    # Google Maps API Json Payload
    path('json_payload/', views.json_payload)


]
