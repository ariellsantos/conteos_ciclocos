# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Conteo, CantidadConteo

def index(request):
    
    return render(request, 'conteo_ciclico/dashboard/index.html')

def conteos(request, estatus=None):
    usuario = request.user
    abiertos = ['abierto', 'proceso']
    cerrados = ['terminado', 'cancelado']
    conteos = None
    print estatus
    if estatus == "abiertos":
        print "hola aqui estoy"
        if usuario.perfil.puesto.nombre == "Contador":
            print "hola soy contador"
            conteos = Conteo.objects.filter(estatus__in=abiertos, contador=usuario)
        elif usuario.perfil.puesto.nombre == "Encargado almacen":
            conteos = Conteo.objects.filter(estatus__in=abiertos)
    elif estatus == "cerrados":
        if usuario.perfil.puesto.nombre == "Contador":
            conteos = Conteo.objects.filter(estatus__in=cerrados, contador=usuario)
        elif usuario.perfil.puesto.nombre == "Encargado almacen":
            conteos = Conteo.objects.filter(estatus__in=cerrados)

    context = {
        'conteos': conteos,
    }

    return render(request, 'conteo_ciclico/conteos/conteos.html',context)


def cantidad_conteos(request, pk):
    return render(request, 'conteo_ciclico/conteos/cantidad_conteos.html')