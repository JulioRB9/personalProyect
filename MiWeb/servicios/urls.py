# URLS de proyecto servicios
from django.urls import path      # Path para importar la APP
from . import views  # importar las vistas de la aplicacion servicios

urlpatterns = [
    path('',views.servicios, name="Servicios" ),
]
