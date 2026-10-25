from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
