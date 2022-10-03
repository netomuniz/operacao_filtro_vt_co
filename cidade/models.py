from django.db import models


class Estado(models.Model):
    estado = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.estado


class Cidade(models.Model):
    uf = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)    

    def __str__(self) -> str:
        return self.cidade


class Area(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.area
