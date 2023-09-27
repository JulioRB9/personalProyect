from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

import datetime

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre_Persona = nombre
        self.apellido_Persona = apellido
        

def viewHtml(request): # Funcion primera vista

    p1 = Persona("Julio", "Rivera Bautista")
    temas = ["Plantillas","Modelo","Formularios","Vista","Despliegue"]
    # nombre_Persona = "Julio"
    # apellido_Persona = "Rivera Bautista"
    fechaActual = datetime.datetime.now()
    # doc_externo = open("/home/jrb/Documents/personalProyect/plantilla/miplantilla.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    # ctx = Context({"nombreVista":p1.nombre_Persona, "apellido":p1.apellido_Persona, "fecha":fechaActual,"temas":temas})
    
    # doc_externo = get_template("miplantilla.html")
    # documento = doc_externo.render({"nombreVista":p1.nombre_Persona, "apellido":p1.apellido_Persona, "fecha":fechaActual,"temas":temas})
    # return HttpResponse(documento)
    return render(request, "miplantilla.html",{"nombreVista":p1.nombre_Persona, "apellido":p1.apellido_Persona, "fecha":fechaActual,"temas":temas})
    
# -------------------------------------------------------------------------------------------#
# Creando vista personalizada la el navegador
def primeraVista(request):
    fechaActual = datetime.datetime.now()
    
    return render(request,"testDev.html",{"dameFecha":fechaActual})

# Segunda vista personalizada para el navegador
def segundaVista(request):
    fechaActual = datetime.datetime.now()
    return render(request,"blog.html",{"dameFecha":fechaActual})

# -------------------------------------------------------------------------------------------#

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