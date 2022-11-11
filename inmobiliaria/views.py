from pickle import NONE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView

# Create your views here.


#crear una funcion solicitar y devolver un texto
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/index.html', {'empleados': empleados})

def crearEmpleado(request):
    formulario = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('empleados')
    return render(request, 'empleados/crear.html', {'formulario': formulario})

def editarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    formulario = EmpleadoForm(request.POST or None, request.FILES or None, instance=empleado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('empleados')
    
    return render(request, 'empleados/editar.html',  {'formulario': formulario})

def eliminarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleados')


def departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/index.html', {'departamentos': departamentos})

def crearDepartamento(request):
    formulario = DepartamentoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('departamentos')
    return render(request, 'departamentos/crear.html', {'formulario': formulario})

def editarDepartamento(request, id):
    departamento = Departamento.objects.get(id=id)
    formulario = DepartamentoForm(request.POST or None, request.FILES or None, instance=departamento)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('departamentos')
    return render(request, 'departamentos/editar.html',  {'formulario': formulario})

def eliminarDepartamento(request, id):
    departamento = Departamento.objects.get(id=id)
    departamento.delete()
    return redirect('departamentos')


def cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'cargos/index.html', {'cargos': cargos})

def crearCargo(request):
    formulario = CargoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cargos')
    return render(request, 'cargos/crear.html', {'formulario': formulario})

def editarCargo(request, id):
    cargo = Cargo.objects.get(id=id)
    formulario = CargoForm(request.POST or None, request.FILES or None, instance=cargo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cargos')
    return render(request, 'cargos/editar.html',  {'formulario': formulario})

def eliminarCargo(request, id):
    cargo = Cargo.objects.get(id=id)
    cargo.delete()
    return redirect('cargos')

