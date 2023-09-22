from django.http import HttpResponse
import datetime

def saludos(request): # Funcion primera vista
    documento = """
    <htmlt>
    <body>
    <h1>Hola Alumnos estes es nuetra pagina de Django</h1>
    </body>
    </htmlt> """
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta Luego amigos....!")

def dameFecha(request):
     
    fechaActual = datetime.datetime.now()
    documento = """
    <htmlt>
    <body>
    <h1>
    La fecha Actual %s
    </h1>
    </body>
    </htmlt> """ % fechaActual
    return HttpResponse(documento)

def calculaEdad(request,edad, agno):

    # agnoActual = 27
    periodo = agno - 2023
    agnoFuturo = edad + periodo

    docmento = """
    <html>
    <body>
    <h1>
    En el año % s 
    tendras  % s años
    </h1>
    </body>
    </html>""" % (agno, agnoFuturo)

    return HttpResponse(docmento)