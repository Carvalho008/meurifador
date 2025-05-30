from django.db import models

class NumeroRifa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    nome = models.CharField(max_length=100, blank=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero} - {self.nome or 'Disponível'} {'(Pago)' if self.pago else '(Não pago)'}"
