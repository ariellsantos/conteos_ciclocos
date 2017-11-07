# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Puesto(models.Model):
    """Model definition for Puesto."""

    nombre = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Puesto."""

        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'

    def __unicode__(self):
        """Unicode representation of Puesto."""
        return self.nombre
