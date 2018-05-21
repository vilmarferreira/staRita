from django.shortcuts import render
from django.views.generic import TemplateView
from noticias.models import Noticia
from galeria.models import foto

def index(request):
    obj = Noticia.objects.all()
    noticias = obj.filter(categoria__nome='Noticias')
    ftsDestaques = obj.filter(categoria__nome='Destaque')[:4]
    eventos = obj.filter(categoria__nome='Eventos')
    context = {

        'noticias': noticias,
        'ftsDestaques': ftsDestaques,
        'eventos': eventos,
    }
    return render(request,'index.html',context)

