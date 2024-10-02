# URLS de proyecto principal
from django.urls import path      # Path para importar la APP
from ProyectoWebApp import views  # importar

from django.conf import settings  # Agregar la URL de los archivos de configuracion setting
from django.conf.urls.static import static #Agregar la configuracion de los archivos estaticos

urlpatterns = [
    path('',views.inicio, name="Inicio" ),
    path('tienda/',views.tienda, name="Tienda" ),
    path('contacto/',views.contacto, name="Contacto" ),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)