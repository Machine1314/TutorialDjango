from django.db import models

# Create your models here.
class EquipoLab(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Equipo')

    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=100, verbose_name='Estado')
    equipo = models.ForeignKey(EquipoLab, null=True, blank=True, on_delete=models.SET_NULL,
                               verbose_name='Equipo Prestado')
    fechaInicio = models.DateField(verbose_name='Fecha Inicio')
    fechaFin = models.DateField(verbose_name='Fecha Fin')
    fechaEntrega = models.DateField(verbose_name='Fecha Entrega', null=True)
    usuario = models.CharField(max_length=100, verbose_name='Usuario que realiza el prestamo')