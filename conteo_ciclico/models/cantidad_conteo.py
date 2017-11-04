from __future__ import unicode_literals

from django.db import models
from .conteo import Conteo
from .ubicaciones import Ubicacion

class CantidadConteo(models.Model):
    conteo = models.ForeignKey(Conteo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'CantidadConteo'
        verbose_name_plural = 'CantidadesConteos'