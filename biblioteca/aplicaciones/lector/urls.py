from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('prestamo/add/', views.RegistarPrestamo.as_view(), name="add"),
    path('prestamov/add/', views.RegistarPrestamoValidacion.as_view(), name="addV"),
    path('prestamom/add/', views.RegistroMultiplePrestamo.as_view(), name="addM"),
]