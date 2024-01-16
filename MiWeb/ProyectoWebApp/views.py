from django.shortcuts import render, HttpResponse

# Create your views here.   
def inicio(request):
    return render(request, 'ProyectoWebApp/inicio.html')

# Create your views here.
def servicios(request):
    return render(request, 'ProyectoWebApp/servicios.html')

# Create your views here.
def tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html')

# Create your views here.
def blog(request):
    return render(request, 'ProyectoWebApp/blog.html')

# Create your views here.
def contacto(request):
    return render(request, 'ProyectoWebApp/contactos.html')


