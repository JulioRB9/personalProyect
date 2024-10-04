from django.contrib import admin
from .models import categorias, Post # Importar el modelo de aplicacions 

# Register your models here.
#Construir panel de administracion
class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(categorias,CategoriasAdmin) # Registramos la app de categorias en el panel de adminstracion
admin.site.register(Post,PostAdmin) # Registramos la app de post en el panel de adminstracion