# URLS de proyecto
from django.urls import path      # Path para importar la APP
from ProyectoWebApp import views  # importar las vistas de la aplicacion

urlpatterns = [
    path('',views.inicio, name="Inicio" ),
    path('servicios/',views.servicios, name="Servicios" ),
    path('tienda/',views.tienda, name="Tienda" ),
    path('blog/',views.blog, name="Blog" ),
    path('contacto/',views.contacto, name="Contacto" ),
]