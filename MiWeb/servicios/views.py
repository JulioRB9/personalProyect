from django.shortcuts import render
from servicios.models import servicio
# Create your views here.
#V* -> Como usao universal de variable
def servicios(request):
    VServicios = servicio.objects.all()    # Importe todo los objetos que le indicamos en el modelos,py
    return render(request, 'servicios/servicios.html',{"servicios":VServicios})