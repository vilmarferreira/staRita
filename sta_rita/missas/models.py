from django.db import models

# Create your models here.

class diaSemana (models.Model):
    nomeDIa = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeDIa

class Missa(models.Model):
    diaSemana = models.ForeignKey(diaSemana, on_delete=models.CASCADE)
    horarioMissa = models.CharField(max_length=200)
    localMissa = models.CharField(max_length=200)

    def __str__(self):
        return self.localMissa



