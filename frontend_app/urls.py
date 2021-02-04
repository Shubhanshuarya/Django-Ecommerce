from django.urls import path
from frontend_app import views

urlpatterns = [
    path('', views.home),
]