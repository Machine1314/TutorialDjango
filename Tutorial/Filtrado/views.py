from django.db import connection
from django.shortcuts import render, redirect
from .models import *
import datetime
import pytz


# Create your views here.
def start(request):
    deudores = []
    begin = None
    end = None
    agregar = False
    today = datetime.datetime.now(pytz.timezone("America/Guayaquil")).date().strftime('%Y-%m-%d')
    today = datetime.datetime.strptime(today, '%Y-%m-%d').date()
    zona = 'America/Guayaquil'
    with connection.cursor() as cursor:
        cursor.execute('SET TIMEZONE="{}"'.format(zona))
    if request.method == 'POST':
        begin = request.POST['begin']
        end = request.POST['end']
        prestamos = Prestamo.objects.filter(fechaInicio__gte=request.POST['begin'], fechaFin__lte=request.POST['end'])
        for prestamo in prestamos:
            if prestamo.fechaEntrega is not None and prestamo.fechaEntrega > prestamo.fechaFin:
                dias = prestamo.fechaEntrega - prestamo.fechaFin
                agregar = True
            elif today > prestamo.fechaFin:
                dias = today - prestamo.fechaFin
                agregar = True
            nombre = prestamo.usuario
            deuda = dias.days * 5
            datos = {'dias': dias.days, 'nombre': nombre, 'deuda': deuda}
            if agregar:
                deudores.append(datos)
            agregar = False
    else:
        prestamos = Prestamo.objects.all()
        for prestamo in prestamos:
            if prestamo.fechaEntrega is not None and prestamo.fechaEntrega > prestamo.fechaFin:
                dias = prestamo.fechaEntrega - prestamo.fechaFin
                agregar = True
            elif today > prestamo.fechaFin:
                dias = today - prestamo.fechaFin
                agregar = True
            nombre = prestamo.usuario
            deuda = dias.days * 5
            datos = {'dias': dias.days, 'nombre': nombre, 'deuda': deuda}
            if agregar:
                deudores.append(datos)
            agregar = False
    context = {'prestamos': prestamos, 'deudores': deudores, 'beginDate': begin, 'endDate': end}
    return render(request, 'Filtrado/Filtrado.html', context)


def handler404(request, exception):
    response = render(request, 'Filtrado/404.html')
    return response


def handler500(request):
    response = render(request, 'Filtrado/500.html')
    return response


def handler403(request, exception):
    response = render(request, 'Filtrado/403.html')
    return response
