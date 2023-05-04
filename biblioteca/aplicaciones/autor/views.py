from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Autor

class ListAutores(ListView):
    model = Autor
    template_name = "autor/autores.html"
    context_object_name = "autores"
    
    def get_queryset(self):
        palabra = self.request.GET.get("nombre", "")
        return Autor.objects.BuscarAutorNombre_Mayor(palabra)
