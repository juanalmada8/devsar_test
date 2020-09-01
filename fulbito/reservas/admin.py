from django.contrib import admin
from .models import Reserva

# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    fields =['cliente', 'cancha', 'empleado','fecha_turno','hora_turno']
    list_display = ['cliente', 'empleado']
    ordering = ['-cliente', '-cancha']
    list_filter = ('cliente', 'cancha',)


admin.site.register(Reserva, ReservaAdmin)
