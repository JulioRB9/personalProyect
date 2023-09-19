from django.http import HttpResponse
def saludos(request): # Funcion primera vista
    return HttpResponse("Hola Alumnos estes es nuetra pagina de Django ")

def despedida(request):
    return HttpResponse("Hasta Luego amigos....!")