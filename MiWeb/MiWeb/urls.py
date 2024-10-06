"""
URL configuration for MiWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# URLS del proyecto
from django.contrib import admin
from django.urls import path,include

# Este es la aplicacion principal donde se va registrar todo las aplicaciones que estemos creando 
# en la applicacion

# Enlazar todas las vistas de nuetras aplicacion
# Ingrediente
# NombreAPPmain + NombreProyecto.urls -> contendra todas las vistas del nuestro aplicacion del proyecto

# 01 - Aplicacion servicios
# 02 - Aplicacion Blog
# 00 - Aplicacion vista Principal 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')), 
    path('',include('ProyectoWebApp.urls')),
]




