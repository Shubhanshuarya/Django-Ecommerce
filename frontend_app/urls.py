from django.urls import path
from frontend_app import views

urlpattern = [
    path('', views.home),
]