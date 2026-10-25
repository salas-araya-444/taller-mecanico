from django.db import models
from ordenes.models import OrdenServicio


class Factura(models.Model):
    orden = models.ForeignKey(
        OrdenServicio,
        on_delete=models.PROTECT,
        related_name='factura',
        unique=True
    )
    numero = models.CharField(max_length=30, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    iva = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'Factura {self.numero}'