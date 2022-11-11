from django.contrib import admin
from .models import Empleado
from .models import Departamento
# Register your models here.
admin.site.register(Departamento)
admin.site.register(Empleado)

