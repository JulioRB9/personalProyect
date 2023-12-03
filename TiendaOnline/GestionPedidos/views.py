from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulo
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormularioContacto
from django.views.decorators.csrf import requires_csrf_token


# Create your views here.
def buscarProductos(request):
    return render(request, "buscar.html")

# Mensaje del servidor conceptual
@requires_csrf_token
def buscar(request):
    c = {}
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
    #     subject =  request.POST["asunto"]
    #     menssage = request.POST["mensaje"] + " " + request.POST["email"]
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = ["inventarios.2023@outlook.com"]
    #     send_mail(subject,menssage,email_from,recipient_list)
    #     return render(request,"gracias.html")
    
    # return render(request, "contacto.html")
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infFormulario = miFormulario.cleaned_data
            send_mail(infFormulario['asunto'],
                    infFormulario['mensaje'],
                    infFormulario.get('email',''),
                    ['inventarios.2023@outlook.com'],)
            return render(request,"gracias.html")
    else:
        miFormulario = FormularioContacto()
    return render(request, "formCont.html",c,{"form":miFormulario})