from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

from vehiculos.models import Vehiculo
from repuestos.models import Repuesto


class OrdenServicio(models.Model):
    ESTADOS = [
        ('RECIBIDA', 'Recibida'),
        ('EN_REPARACION', 'En reparación'),
        ('FINALIZADA', 'Finalizada'),
        ('FACTURADA', 'Facturada'),
    ]

    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.PROTECT,
        related_name='ordenes'
    )
    mecanico = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='ordenes_asignadas'
    )
    falla_reportada = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='RECIBIDA'
    )
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_finalizacion = models.DateTimeField(
        null=True,
        blank=True
    )
    mano_obra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    repuestos = models.ManyToManyField(
        Repuesto,
        through='DetalleOrden',
        related_name='ordenes'
    )

    def __str__(self):
        return f'Orden {self.id} - {self.vehiculo.placa}'


class DetalleOrden(models.Model):
    orden = models.ForeignKey(
        OrdenServicio,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    repuesto = models.ForeignKey(
        Repuesto,
        on_delete=models.PROTECT,
        related_name='detalles_orden'
    )
    cantidad = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    precio_aplicado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['orden', 'repuesto'],
                name='repuesto_unico_por_orden'
            )
        ]

    def __str__(self):
        return f'Orden {self.orden_id} - {self.repuesto.nombre}'