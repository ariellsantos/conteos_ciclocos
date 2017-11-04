# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Pieza, Conteo, Ubicacion,CantidadConteo


@admin.register(Pieza)
class PiezaAdmin(admin.ModelAdmin):
    pass


@admin.register(Conteo)
class ConteoAdmin(admin.ModelAdmin):
    pass

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    pass

@admin.register(CantidadConteo)
class CantidadConteoAdmin(admin.ModelAdmin):
    pass
    
