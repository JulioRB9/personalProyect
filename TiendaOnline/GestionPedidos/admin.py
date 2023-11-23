from django.contrib import admin
from GestionPedidos.models import Cliente,Articulo,Pedido

#Clase para ver los otros campos de nuerto modelo.
class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono") #Nuestra los campos que necesitamos
    search_fields=("nombre","telefono")                            #Muestra un campo de busqueda al que referimos para realizar la consulta

# Register your models here.
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Articulo)
admin.site.register(Pedido)

