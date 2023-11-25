from django.contrib import admin
from GestionPedidos.models import Cliente,Articulo,Pedido

#Clase para ver los otros campos de nuestro modelo.
class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono") #Nuestra los campos que necesitamos
    search_fields=("nombre","telefono")                            #Muestra un campo de busqueda al que referimos para realizar la consulta

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidoAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

# Register your models here.
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Articulo,ArticulosAdmin)
admin.site.register(Pedido,PedidoAdmin)

