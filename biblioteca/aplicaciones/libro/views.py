from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Libro, Categoria

class ListAutores(ListView):
    model = Libro
    template_name = "libro/libros.html"
    context_object_name = "libros"
    
    def get_queryset(self):
        palabra = self.request.GET.get("nombre", "")
        fecha_i = self.request.GET.get("fecha_i", "")
        fecha_f = self.request.GET.get("fecha_f", "")
        if fecha_i and fecha_f:
            return Libro.objects.BuscarLibros_FechaIF(palabra, fecha_i, fecha_f)
        else:
            return Libro.objects.BuscarLibros_Fecha(palabra)
        

class ListCategoria(ListView):
    model = Libro
    template_name = "libro/categorias.html"
    context_object_name = "categorias"
    
    def get_queryset(self):
        return Libro.objects.BuscarLibros_Categoria(1)
    
    
class DetalleCategoria(DetailView):
    model = Libro
    template_name = "libro/detalles.html"
    context_object_name = "libro"

 