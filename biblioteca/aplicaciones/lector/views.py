from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
# Create your views here.
from .models import Prestamo
from .forms import PrestamoForm, MultiplePrestamoForm

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

class RegistarPrestamoValidacion(FormView):
    template_name = 'lector/add.html'
    form_class = PrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        #Validar si ya esta creado un registro, si no existe lo crea        
        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data["lector"],
            libro = form.cleaned_data["libro"],
            devuelto = False,
            defaults={
                'fecha_prestamo' : date.today()
            }
        )
        
        if created:
            return super().form_valid(form)
        else:
            return HttpResponseRedirect('/')
        
        
class RegistroMultiplePrestamo(FormView):
    template_name = 'lector/addMultiple.html'
    form_class = MultiplePrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        libros = form.cleaned_data["libros"]
        prestamos = []
        for libro in libros:
            prestamo = Prestamo(
                lector = form.cleaned_data["lector"],
                libro = libro,
                fecha_prestamo = date.today(),
                devuelto = False
            )
            prestamos.append(prestamo)
            
        #Optimizando un solo guardado para varios modelos
        Prestamo.objects.bulk_create(
            prestamos
        )
        return super().form_valid(form)