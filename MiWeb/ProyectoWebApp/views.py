from django.shortcuts import render, HttpResponse
from servicios.models import servicio

# Create your views here.   
def inicio(request):
    return render(request, 'ProyectoWebApp/inicio.html')

# Create your views here.
# def servicios(request):
#     servicios = servicio.objects.all()
#     return render(request, 'servicios/servicios.html',{"servicios":servicios})

# Create your views here.
def tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html')

# Create your views here.
# def blog(request):
#     return render(request, 'ProyectoWebApp/blog.html')

# Create your views here.
def contacto(request):
    return render(request, 'ProyectoWebApp/contactos.html')


