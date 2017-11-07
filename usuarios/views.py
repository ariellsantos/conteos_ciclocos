# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Perfil
from django.contrib.auth.models import User
from .models import Puesto
from decimal import Decimal

def login_user(request):
    if request.user.is_authenticated():
        return redirect("conteo_ciclico:dashboard")
    else:
        if request.method == "POST":
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                print "si se logeo"
                return redirect("conteo_ciclico:dashboard")
            else:
                
                return render(request, 'usuarios/login.html')
        else:
            return render(request, 'usuarios/login.html')
            
def logout_user(request):
    logout(request)
    return redirect('/')

def guardar_usuario(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username,email,password)
            user.first_name =  request.POST.get('first_name')
            user.email = request.POST.get('email')
            perfil = Perfil()
            perfil.numero_empleado = request.POST.get('numero_empleado')
            perfil.direccion = request.POST.get('direccion')
            perfil.telefono = request.POST.get('telefono')
            puesto = request.POST.get('puesto')
            puesto = Puesto.objects.get(pk=puesto)
            perfil.puesto = puesto
            user.save()                        
            perfil.usuario = user
            perfil.save()
            messages.success(request, 'Se creo el usuario correctamente')
            return redirect("conteo_ciclico:dashboard")
        except ValueError:
            datos = dict(request.POST)
            print datos
            context = {
                'datos': datos
            }
            messages.error(request, 'No se  guardo el usuario, por favor verifica los datos')
            return render(request, 'usuarios/crear_usuario.html', context)
        

    
    elif request.method == "GET":
        puestos = Puesto.objects.all()
        context = {
            'puestos': puestos,
        }
        return render(request, "usuarios/crear_usuario.html", context)

