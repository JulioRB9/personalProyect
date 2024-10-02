from django.contrib import admin
from .models import servicio

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(servicio, ServiciosAdmin) # Registramos la app de servicios en el panel de adminstracion