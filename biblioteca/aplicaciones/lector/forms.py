from django import forms

from .models import Prestamo
from aplicaciones.libro.models import Libro

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = (
            'libro',
            'lector',
        )

class MultiplePrestamoForm(forms.ModelForm):
    
    libros = forms.ModelMultipleChoiceField(
        queryset = None,
        required = True,
        widget = forms.CheckboxSelectMultiple,
    )
    
    #Inicializando el formulario
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.all()
    
    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )
