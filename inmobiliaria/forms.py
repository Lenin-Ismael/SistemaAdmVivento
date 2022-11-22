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
            'identificacion': forms.TextInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'cargo': forms.Select(attrs={'class':'form-control'}),
            'departamento': forms.Select(attrs={'class':'form-control'}),
            'imagen': forms.FileInput(attrs={'class':'form-control'}),
        }

