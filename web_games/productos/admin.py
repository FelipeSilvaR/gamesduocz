from django.contrib import admin

# Register your models here.
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    #agregar restricciones del administrador
    #que cosas el ususario no puede editar
    readonly_fields = ('created','updated')
#registra el modelo para ser administrado
admin.site.register(Producto, ProductoAdmin)