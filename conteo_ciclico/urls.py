from django.conf.urls import url
from . import views

app_name = "conteo_ciclico"

urlpatterns = [
    url('^$', views.index, name="dashboard" ),
    url('^conteos/(?P<estatus>[\w\-]+)/$', views.conteos, name="conteos"),
    url('^cantidad_conteso/(?P<pk>\d+)/$', views.cantidad_conteos, name="cantidad_conteos"),
    url('^anadir_conteos/(?P<pk>\d+)/$', views.add_conteos, name="anadir_conteos"),
]