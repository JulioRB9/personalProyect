# URLS de proyecto principal
from django.urls import path      # Path para importar la APP
from . import views  # importar las vistas de la aplicacion


urlpatterns = [
    path('',views.blog, name="Blog" ),
]
