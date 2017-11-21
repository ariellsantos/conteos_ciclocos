from django.conf.urls import url
from . import views

app_name = "conteo_ciclico"

urlpatterns = [
    url(r'^$', views.index, name="dashboard" ),
    url(r'^conteos/(?P<estatus>[\w\-]+)/$', views.conteos, name="conteos"),
    url(r'^cantidad_conteos/(?P<pk>\d+)/$', views.cantidad_conteos, name="cantidad_conteos"),
    url(r'^anadir_conteos/(?P<pk>\d+)/$', views.add_conteos, name="anadir_cantidad_conteos"),
    url(r'^cerrar_conteo/(?P<pk>\d+)/$', views.cerrar_conteo, name="cerrar_conteo"),
    url(r'^crear_conteo/', views.crear_conteo, name="crear_conteo"),
]