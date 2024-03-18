from django.shortcuts import render
from servicios.models import servicio
# Create your views here.
def servicios(request):
    servicios = servicio.objects.all()
    return render(request, 'servicios/servicios.html',{"servicios":servicios})