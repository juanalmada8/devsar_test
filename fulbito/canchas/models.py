from django.db import models
from django.utils.timezone import now

# Create your models here.

class Cancha(models.Model):
    nombre = models.CharField(max_length=100, verbose_name = "Nombre")
    codigo_interno = models.CharField(max_length=100, verbose_name = "Codigo")
    tipo_cancha = models.CharField(max_length=80, verbose_name = "Tipo de Cancha")
    vestuario = models.BooleanField(default=False, verbose_name = "Vestuario")
    iluminacion = models.BooleanField(default=False, verbose_name = "Iluminacion")
    cesped_sintetico = models.BooleanField(default=False, verbose_name = "Tipo de Cesped")
    ruta_imagen = models.FileField(upload_to='fotos/%Y/%m/%d', default='defecto/defecto.jpg', blank=True, null=True, verbose_name = "Imagen")
    fecha_create = models.DateTimeField(auto_now_add=True, verbose_name = "Creacion")
    fecha_update = models.DateTimeField(auto_now=True, verbose_name = "Update")

    class Meta:
        verbose_name = "cancha"
        verbose_name_plural = "canchas"
        ordering = ['-fecha_create']   # Ordenados desde el mas reciente al mas antiguo   
    
    def _str_(self):
        return self.nombre