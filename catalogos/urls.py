from django.urls import path
from catalogos.views import *

from catalogos import views 


urlpatterns = [
    path('oficina/list', OficinaView.as_view(), name='oficinaList'),
    path('oficina/create', OficinaCreate.as_view(), name='oficinaCreate'),     
    path('oficina/edit/<int:pk>', OficinaUpdate.as_view(), name='oficinaEdit'),
    path('oficina/delete/<int:pk>', OficinaDelete.as_view(), name='oficinaDelete'),
    
    
    path('', views.homeCatalogos, name='homeCatalogos'),
    #rutas para el CRUD de Vehiculo
    path('vehiculo/list', VehiculoView.as_view(), name='vehiculoList'),
    path('vehiculo/create', VehiculoCreate.as_view(), name='vehiculoCreate'),
    path('vehiculo/delete/<int:pk>', VehiculoDelete.as_view(), name='vehiculoDelete'),
    path('vehiculo/update/<int:pk>', VehiculoUpdate.as_view(), name='vehiculoUpdate'),
    
    # Rutas para el CRUD de Propietario
    path('propietario/list', PropietarioView.as_view(), name='propietarioList'),
    path('propietario/create', PropietarioCreate.as_view(), name='propietarioCreate'),   
    path('propietario/delete/<int:pk>', PropietarioDelete.as_view(), name='propietarioDelete'),
    path('propietario/update/<int:pk>', PropietarioUpdate.as_view(), name='propietarioUpdate'),   
    
    # Rutas para el CRUD de placas
    path('placa/list', PlacaView.as_view(), name='placaList'),
    path('placa/create', PlacaCreate.as_view(), name='placaCreate'),   
    path('placa/delete/<int:pk>', PlacaDelete.as_view(), name='placaDelete'),
    path('placa/update/<int:pk>', PlacaUpdate.as_view(), name='placaUpdate'),   
           
    
]
