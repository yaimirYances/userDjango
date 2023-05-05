from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('prestamo/add/', views.RegistarPrestamo.as_view(), name="add"),
]