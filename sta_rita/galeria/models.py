
from django.urls import reverse
from django.db import models
from datetime import datetime
from django_thumbs.db.models import ImageWithThumbsField
#from django_thumbs.db.models import ImageWithThumbsFieldFile

# Create your models here.
class Album(models.Model):
    titulo = models.CharField(u'Titulo', max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    data = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('fotos:album1', kwargs={'slug': self.slug})

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('titulo',)
        db_table = 'psssv_album'
        verbose_name_plural = 'Albuns'



class foto(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE , null= True, blank=True)
    titulo = models.CharField(u'Titulo', max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True)
    original = ImageWithThumbsField(
        null=True,
        blank=True,
        upload_to='galeria',
        sizes=((125, 125), (200, 200), (500, 500))
    )
    dataPublicacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('album', kwargs={'slug': self.slug})
        return self.original

    def get_exibicao(self):
        nome_arq = str(self.original)
        delimiter = nome_arq.find(".JPG")
        nome_arq = nome_arq[:delimiter] + ".500x500.jpg"
        return nome_arq

    def get_thumbnail(self):
        nome_arq = str(self.original)
        delimiter = nome_arq.find(".JPG")
        nome_arq = nome_arq[:delimiter] + ".125x125.jpg"
        return nome_arq

    class Meta:
        ordering = ('album', 'titulo',)
        db_table = 'psssv_fotos'

#Signals
from django.db.models import signals
from .signals import slug_pre_save
signals.pre_save.connect(slug_pre_save, sender = Album)
signals.pre_save.connect(slug_pre_save, sender = foto)
