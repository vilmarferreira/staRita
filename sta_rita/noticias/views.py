from django.shortcuts import render
from django.views import generic

from .models import Noticia

# Create your views here.



class NewsListView(generic.ListView):
    model = Noticia
    template_name = 'noticias/noticias.html'
    paginate_by = 10

    def get_queryset(self):
        return Noticia.objects.filter(categoria__nome='Noticias')


newsList= NewsListView.as_view()


class EventosListView(generic.ListView):
    model = Noticia
    template_name = 'noticias/eventos.html'
    paginate_by = 10

    def get_queryset(self):
        return Noticia.objects.filter(categoria__nome='Eventos')
eventosList= EventosListView.as_view()


def noticiaEspecifica(request,slug):

    newNoticia = Noticia.objects.get(slug=slug)
    context = {
        'noticia':newNoticia,
    }
    return render(request,'noticias/noticia.html',context)

