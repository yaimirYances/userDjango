from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('libros/', views.ListAutores.as_view(), name="libros"),
    path('categorias/', views.ListCategoria.as_view(), name="categorias"),
    path('detalles/<pk>', views.DetalleCategoria.as_view(), name="detalles"),
]