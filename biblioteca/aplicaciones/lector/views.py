from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
# Create your views here.
from .models import Prestamo
from .forms import PrestamoForm

class RegistarPrestamo(FormView):
    template_name = 'lector/add.html'
    form_class = PrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        #Crear de cero un nuevo registro
        # Prestamo.objects.create(
        #     lector = form.cleaned_data["lector"],
        #     libro = form.cleaned_data["libro"],
        #     fecha_prestamo = date.today(),
        #     devuelto = False
        # )
        
        #Guarda un registro en la base de datos, si ya existe 
        #lo actualiza
        prestamo = Prestamo(
            lector = form.cleaned_data["lector"],
            libro = form.cleaned_data["libro"],
            fecha_prestamo = date.today(),
            devuelto = False
        )
        prestamo.save()
        
        #disminuir stock
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock -1
        libro.save()
        
        
        return super().form_valid(form)

