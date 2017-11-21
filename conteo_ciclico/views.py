# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
from threading import Thread
import requests
from .hilos import ThreadCSV
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Conteo, CantidadConteo, Ubicacion, Pieza
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

@login_required
def index(request):
    
    return render(request, 'conteo_ciclico/dashboard/index.html')

@login_required
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


@login_required
def cantidad_conteos(request, pk):
    conteo = Conteo.objects.get(pk=pk)
    cantidades_conteo = CantidadConteo.objects.filter(conteo=conteo)
    
    context = {
        'conteo': conteo,
        'cantidades': cantidades_conteo,
    }

    return render(request, 'conteo_ciclico/conteos/cantidad_conteos.html', context)


@login_required
def add_conteos(request, pk):
    conteo = Conteo.objects.get(pk=pk)
    ubicaciones = Ubicacion.objects.all()
    context = {
        'conteo': conteo,
        'ubicaciones': ubicaciones,
    }
    if request.method == "GET":
        return render(request, 'conteo_ciclico/conteos/anadir_conteos.html', context)
    elif request.method == "POST":
        cantidad = int(request.POST.get('cantidad', 0))
        ubicacion = request.POST.get('ubicacion')
        ubicacion = Ubicacion.objects.get(pk=ubicacion)

        cantidad_conteo = CantidadConteo()
        cantidad_conteo.cantidad = cantidad
        cantidad_conteo.conteo = conteo
        cantidad_conteo.ubicacion = ubicacion
        cantidad_conteo.save()
        conteo.cantidad_fisico = conteo.cantidad_fisico + cantidad
        conteo.save()
        
        messages.success(request, 'Se agrego correctamente')
        return redirect("conteo_ciclico:conteos", "abiertos")

@login_required
def cerrar_conteo(request, pk):
    conteo = Conteo.objects.get(pk=pk)
    conteo.estatus = "terminado"
    conteo.save()
    messages.error(request, 'Se cerro el conteo')
    return redirect("conteo_ciclico:conteos", "cerrados")


@login_required
def crear_conteo(request):
    contadores = User.objects.filter(perfil__puesto__nombre="Contador")
    piezas = Pieza.objects.all()
    context = {
        'contadores': contadores,
        'piezas': piezas,
    }
    if request.method == "GET":
        return render(request, 'conteo_ciclico/conteos/crear_conteo.html', context)
    elif request.method == "POST":
        pieza = request.POST.get('pieza')
        pieza = Pieza.objects.get(pk=pieza)
        contador = request.POST.get('contador')
        contador = User.objects.get(pk=contador)
        cantidad_sap = int(request.POST.get('cantidad_sap'))

        conteo = Conteo()
        conteo.pieza = pieza
        conteo.contador = contador
        conteo.cantidad_sap = cantidad_sap
        conteo.save()
        message = "Se ha agregado un nuevo conteo de la pieza <span style='color:red;'>{}</span> , en el SAP hay {}".format(conteo.pieza, conteo.cantidad_sap)
        hilo = Thread(target=_send_email, args=(contador.email, message))
        hilo.start()
        messages.success(request, 'Se  correctamente creo correctamente el conteo')
        return redirect("conteo_ciclico:conteos", "abiertos")


def _send_email(email, message):
    print settings.MAILGUN_KEY
    email_sent = requests.post(
        "https://api.mailgun.net/v3/correo.com/messages",
        auth=("api", settings.MAILGUN_KEY),
        data={"from": "Lennox Inc. <hola@corroeo.com>",
              "to": [email],
              "subject": "Mensaje del trabajo",
              "html": message,
              "o:tracking:": True})
    
    print email_sent.status_code
    print "Hola"
    return email_sent

