from xml.dom.minidom import Document
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    
    path('cargos', views.cargos, name='cargos'),
    path('cargos/crearCargo', views.crearCargo, name='crearCargo'),
    path('cargos/editarCargo/', views.editarCargo, name='editarCargo'),
    path('cargos/editarCargo/<int:id>', views.editarCargo, name='editarCargo'),
    path('eliminarCargo/<int:id>', views.eliminarCargo, name='eliminarCargo'),

    path('departamentos', views.departamentos, name='departamentos'),
    path('departamentos/crearDepartamento', views.crearDepartamento, name='crearDepartamento'),
    path('departamentos/editarDepartamento/', views.editarDepartamento, name='editarDepartamento'),
    path('departamentos/editarDepartamento/<int:id>', views.editarDepartamento, name='editarDepartamento'),
    path('eliminarDepartamento/<int:id>', views.eliminarDepartamento, name='eliminarDepartamento'),

    
    path('empleados', views.empleados, name='empleados'),
    path('empleados/crearEmpleado', views.crearEmpleado, name='crearEmpleado'),
    path('empleados/editarEmpleado/', views.editarEmpleado, name='editarEmpleado'),
    path('empleados/editarEmpleado/<int:id>', views.editarEmpleado, name='editarEmpleado'),
    path('eliminarEmpleado/<int:id>', views.eliminarEmpleado, name='eliminarEmpleado'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 