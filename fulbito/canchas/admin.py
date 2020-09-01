from django.contrib import admin
from .models import Cancha
# Register your models here.


class CanchaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_create', 'fecha_update')# solo mostrar fecha creacion y update desde admin
    fields =['nombre','tipo_cancha', 'codigo_interno','vestuario','iluminacion','cesped_sintetico','ruta_imagen','fecha_create', 'fecha_update']
    list_display = ['nombre', 'tipo_cancha', 'codigo_interno']
    ordering = ['-nombre']
    list_filter = ('nombre', 'tipo_cancha',)

admin.site.register(Cancha, CanchaAdmin)