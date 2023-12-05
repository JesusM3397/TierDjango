from django.contrib import admin

from .models import Inventario, Envio, Solicitud

admin.site.register(Inventario)
admin.site.register(Envio)
admin.site.register(Solicitud)