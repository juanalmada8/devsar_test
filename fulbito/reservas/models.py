from django.db import models

from django.db import models
from django.utils.timezone import now
from canchas.models import  Cancha

# Create your models here.


class Reserva(models.Model):
    #Se intento constriuir la relacion entre canchas y reservas......no se pudo...
    #id = models.AutoField(primary_key=True)
    #cancha = models.ManyToManyField(Cancha, verbose_name = 'Cancha')
    cancha = models.CharField(max_length = 100, verbose_name = 'Cancha')
    cliente = models.CharField(max_length = 100, verbose_name = 'Cliente')
    empleado = models.CharField(max_length = 100, verbose_name = 'Empleado de turno')
    fecha_create = models.DateTimeField(auto_now_add=True)
    fecha_turno = models.DateField(verbose_name="Fecha de Reserva")
    hora_turno = models.TimeField(verbose_name="Hora de Reserva")


    class Meta:
        verbose_name = "reserva"
        verbose_name_plural = "reservas"
        ordering = ['-fecha_create']
    
    def _str_(self):
        return self.cliente