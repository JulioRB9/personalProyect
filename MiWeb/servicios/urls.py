# URLS de proyecto servicios
from django.urls import path      # Path para importar la APP
from servicios import views  # importar las vistas de la aplicacion servicios
from django.conf import settings  # Agregar la URL de los archivos de configuracion setting
from django.conf.urls.static import static #Agregar la configuracion de los archivos estaticos

urlpatterns = [
    path('',views.servicios, name="Servicios" ),

]
