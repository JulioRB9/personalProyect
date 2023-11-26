from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulo

# Create your views here.
def buscarProductos(request):
    return render(request, "buscar.html")

# Mensaje del servidor conceptual
def buscar(request):
    if request.GET["producto"]:
        # mensaje="El producto buscado: %r" %request.GET["producto"]
        producto = request.GET["producto"]
        # Limitar palabras en el campo de busqueda
        if len(producto)>20:
            mensaje = "Texto demasiado largo"
        else:
            articulo = Articulo.objects.filter(nombre__iexact=producto)
            return render(request, "busquedaBBDD.html",{"articulos":articulo, "query":producto})
    else:
        mensaje = "No instroducido datos"
    

    return HttpResponse(mensaje)