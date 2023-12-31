from django.shortcuts import render, HttpResponse, redirect
from .models import Vehiculo, Propietario, Oficina, Placa
from .forms import VehiculoForm, PropietarioForm, OficinaForm, PlacaForm

from django.views import generic 
from django.urls  import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin  


# Create your views here.
def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

# -----------------------------------------------------------------------------

class OficinaView(LoginRequiredMixin,generic.ListView): 
    model =  Oficina
    queryset = Oficina.objects.all()
    template_name = 'oficinaList.html'
    context_object_name = 'oficinas'

class OficinaCreate(generic.CreateView):
    model = Oficina
    template_name = 'oficinaCreate.html'
    context_object_name = 'oficinas'
    form_class = OficinaForm
    success_url = reverse_lazy("oficinaList")
    
class OficinaUpdate(generic.UpdateView):
    model = Oficina
    template_name = 'oficinaCreate.html'
    context_object_name = 'oficinas'
    form_class = OficinaForm
    success_url = reverse_lazy('oficinaList')

class OficinaDelete(generic.DeleteView):
    model = Oficina
    template_name = 'oficinaDelete.html'
    context_object_name = 'oficinas'
    success_url = reverse_lazy('oficinaList')
    

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

# -----------------------------------------------------------------------------

class VehiculoView(LoginRequiredMixin,generic.ListView): 
    model =  Vehiculo
    queryset = Vehiculo.objects.all()
    template_name = 'vehiculoList.html'
    context_object_name = 'vehiculos'

class VehiculoCreate(generic.CreateView):
    model = Vehiculo
    template_name = 'vehiculoCrear.html'
    context_object_name = 'vehiculos'
    form_class = VehiculoForm
    success_url = reverse_lazy("vehiculoList")
    
class VehiculoUpdate(generic.UpdateView):
    model = Vehiculo
    template_name = 'vehiculoCrear.html'
    context_object_name = 'vehiculos'
    form_class = VehiculoForm
    success_url = reverse_lazy('vehiculoList')

class VehiculoDelete(generic.DeleteView):
    model = Vehiculo
    template_name = 'vehiculoDelete.html'
    context_object_name = 'vehiculos'
    success_url = reverse_lazy('vehiculoList')


# -----------------------------------------------------------------------------
class PropietarioView(LoginRequiredMixin,generic.ListView): 
    model =  Propietario
    queryset = Propietario.objects.all()
    template_name = 'propietarioList.html'
    context_object_name = 'propietarios'

class PropietarioCreate(generic.CreateView):
    model = Propietario
    template_name = 'propietarioCrear.html'
    context_object_name = 'propietarios'
    form_class = PropietarioForm
    success_url = reverse_lazy("propietarioList")
    
class PropietarioUpdate(generic.UpdateView):
    model = Propietario
    template_name = 'propietarioCrear.html'
    context_object_name = 'propietarios'
    form_class = PropietarioForm
    success_url = reverse_lazy('propietarioList')

class PropietarioDelete(generic.DeleteView):
    model = Propietario
    template_name = 'propietarioDelete.html'
    context_object_name = 'propietarios'
    success_url = reverse_lazy('propietarioList')

# -----------------------------------------------------------------------------

class PlacaView(LoginRequiredMixin,generic.ListView): 
    model =  Placa
    queryset = Placa.objects.all()
    template_name = 'placaList.html'
    context_object_name = 'placas'

class PlacaCreate(generic.CreateView):
    model = Placa
    template_name = 'placaCrear.html'
    context_object_name = 'placas'
    form_class = PlacaForm
    success_url = reverse_lazy("placaList")
    
class PlacaUpdate(generic.UpdateView):
    model = Placa
    template_name = 'placaCrear.html'
    context_object_name = 'placas'
    form_class = PlacaForm
    success_url = reverse_lazy('placaList')

class PlacaDelete(generic.DeleteView):
    model = Placa
    template_name = 'placaDelete.html'
    context_object_name = 'placas'
    success_url = reverse_lazy('placaList')


# -----------------------------------------------------------------------------