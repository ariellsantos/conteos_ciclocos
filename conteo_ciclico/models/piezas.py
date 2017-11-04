# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pieza(models.Model):
    
    UNIDADES = (
        ('kg', 'KG'),
        ('pieza', 'Pieza'),
        ('contenedor', 'Contenedor'),
        ('caja', 'Caja'),
        ('tonel', 'Tonel'),
    )

    nombre = models.CharField(max_length=50)
    numero_pieza = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)   
    unidad = models.CharField(max_length=50, choices=UNIDADES)
    piezas_unidad = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pieza'
        verbose_name_plural = 'Piezas'