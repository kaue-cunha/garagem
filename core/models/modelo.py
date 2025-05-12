from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        marca = self.marca.upper() if self.marca else ""
        nome = self.nome.upper()
        return f"{self.id} - {marca} {nome}".strip()