# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Ubicacion(models.Model):
    
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'