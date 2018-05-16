from django.db import models


# Create your models here.
from categorias.models import Categoria



class Noticia(models.Model):
    tituloNoticia = models.CharField(max_length=200)
    descricao = models.TextField(null=True,blank=True)
    paroquia = models.CharField(max_length=200)
    data = models.DateTimeField(null=True, blank=True)
    banner = models.ImageField (upload_to='banner_noticia', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    dataPublicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tituloNoticia

