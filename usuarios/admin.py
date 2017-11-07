# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Perfil, Puesto
from django.contrib.auth.models import User


admin.site.unregister(User)

class PerfilAdminInline(admin.StackedInline):
    model = Perfil

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        PerfilAdminInline,
    ]


@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    pass