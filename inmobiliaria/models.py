from django.db import models

# Create your models here.

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,verbose_name='Código')
    nombre = models.CharField(max_length=250,verbose_name='Nombre')
    actividad = models.CharField(max_length=500,verbose_name='Actividad')


    def __str__(self):
        fila = self.nombre
        return fila


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,verbose_name='Código')
    nombre = models.CharField(max_length=250,verbose_name='Nombre')
    actividad = models.CharField(max_length=500,verbose_name='Actividad')

    def __str__(self):
        fila = self.nombre
        return fila
   
class Meta:
    verbose_name_plural = 'Departamentos'   
    ordering = ['id']

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=10,verbose_name='Identificación')
    nombres = models.CharField(max_length=250,verbose_name='Nombres')
    apellidos = models.CharField(max_length=250,verbose_name='Apellidos')
    cargo = models.ForeignKey(Cargo, verbose_name='Cargos', null=False, blank=False, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, verbose_name='Departamentos', null=False, blank=False, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)

    def __str__(self):
        fila = "Nombres:  " + self.nombres + " " + " - Apellidos: " + self.apellidos
        return fila




