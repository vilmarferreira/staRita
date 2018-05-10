from django.db import models

# Create your models here.
class Evento(models.Model):
    nomeEvento = models.CharField(max_length=200)
    descricao = models.TextField()
    paroquia = models.CharField(max_length=200)
    data = models.DateTimeField()
    banner = models.ImageField (upload_to='banner_eventos', null=True, blank=True)

    def __str__(self):
        return self.nomeEvento

