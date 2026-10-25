from django.db import models
from clientes.models import Cliente


class Vehiculo(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='vehiculos'
    )
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    anio = models.PositiveIntegerField()
    kilometraje = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.placa} - {self.marca} {self.modelo}'
