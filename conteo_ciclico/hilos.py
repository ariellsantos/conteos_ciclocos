import Queue
from threading import Thread
import csv

from django.shortcuts import render, redirect, HttpResponse
from .models import Conteo, CantidadConteo, Ubicacion, Pieza

class ThreadCSV(object):
    queue = Queue.Queue()

    def __init__(self, conteo):
        self.conteo = conteo
    
    def create_thread(self):
        hilo = Thread(target=self._export_csv, args=(self.conteo,)).start()
        result = self.queue.get()
        return  result
        
        
    def _export_csv(self, conteo):
        
        conteo = Conteo.objects.get(pk=conteo)
        cantidades_conteo = CantidadConteo.objects.filter(conteo=conteo)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=conteos.csv'
        writer = csv.writer(response)
        writer.writerow(["Pieza", "Cantidad", 'Ubicacion' ,"Fecha"])
        for conteo in cantidades_conteo:
            writer.writerow([conteo.conteo.pieza, conteo.cantidad, conteo.ubicacion, conteo.fecha, ])
        print "Hola aqui estoy"
        return self.queue.put(response)