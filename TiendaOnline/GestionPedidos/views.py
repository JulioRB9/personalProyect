from django.shortcuts import render


# Create your views here.
def buscarProductos(request):
    return render(request, "buscar.html")