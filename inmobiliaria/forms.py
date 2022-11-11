from django import forms
from .models import Empleado
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('__all__')

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'id',
            'identificacion',
            'nombres',
            'apellidos',
            'cargo',
            'departamento',
            'imagen',
        ]
        labels = {
            'id' : 'Id',
            'identificacion': 'Identificación',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cargo': 'Cargo',
            'departamento': 'Departamento',
            'imagen': 'Imagen',
        }
        widgets={
        }
     


