from django import forms
from .models import *

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ('__all__')

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('__all__')

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('__all__')
        widgets= {
            'cargo': forms.Select(attrs={'class':'form-control'}),
            'departamento': forms.Select(attrs={'class':'form-control'})

        }

     


