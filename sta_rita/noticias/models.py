from django.db import models


# Create your models here.
from categorias.models import Categoria
from django.urls import reverse


class Noticia(models.Model):
    tituloNoticia = models.CharField(u'Titulo',max_length=200)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    descricao = models.TextField(null=True,blank=True)
    paroquia = models.CharField(max_length=200)
    data = models.DateTimeField(null=True, blank=True)
    imgNoticia = models.ImageField (upload_to='banner_noticia', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    dataPublicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tituloNoticia

    def get_absolute_url(self):
        return reverse('noticias:noticiaEspecifica', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.tituloNoticia






from django.db.models import signals
from galeria.signals import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender = Noticia)

