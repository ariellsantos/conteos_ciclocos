# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('conteo_ciclico:dashboard')
    else:
        return render(request, "basicos/index.html")
