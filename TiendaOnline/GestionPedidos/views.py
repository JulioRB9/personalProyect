from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulo
from django.core.mail import send_mail
from django.conf import settings

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

# Vista contacto
def contacto(request):
    if request.method == "POST":
        subject =  request.POST["asunto"]
        menssage = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["za17011672@zapopan.tecmm.edu.mx"]
        send_mail(subject,menssage,email_from,recipient_list)
        return render(request,"gracias.html")
    
    return render(request, "contacto.html")
