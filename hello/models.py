# hello/models.py
from django.db import models

class Saludo(models.Model):
    texto     = models.CharField(max_length=120)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
