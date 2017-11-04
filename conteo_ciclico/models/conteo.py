# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from .piezas import Pieza



class Conteo(models.Model):
    ESTATUS = (
        ('abierto', 'Abierto'),
        ('proceso', 'En proceso'),
        ('terminado', 'Terminado'),
        ('cancelado', 'Cancelado'),
    )

    PRIORIDAD = (
        ('programa', 'Programa'),
        ('especial', 'Especial'),
        ('critico', 'Critico'),
    )


    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    contador = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad_fisico = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    fecha_creacion = models.DateTimeField(auto_now=True)
    estatus = models.CharField(max_length=50, choices=ESTATUS, default='abierto')
    prioridad = models.CharField(max_length=50, choices=PRIORIDAD, default='programa')
    cantidad_sap = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return "Pieza: {} Contador: {} ".format(self.pieza, self.contador)

    class Meta:
        verbose_name = 'Conteo'
        verbose_name_plural = 'Conteos'