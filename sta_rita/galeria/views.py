from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext

from .models import Album, foto


def albuns(request):
    lista = Album.objects.all()

    context = {
        'lista': lista,
    }
    return render(request, 'galeria/albuns.html', context)
    # return render(request, 'contact.html', context)



# from django.shortcuts import render_to_response, get_object_or_404
# from django.template import RequestContext
#
# from .models import *
#
#
# def albuns(request):
#     lista = Album.objects.all()
#
#     return render_to_response('raiz/galeria/albuns.html', locals(), context_instance=RequestContext(request))
#
#
# def album(request, slug):
#     album = get_object_or_404(Album, slug=slug)
#     imagens = foto.objects.filter(album=album)
#
#     return render_to_response('raiz/galeria/album.html', locals(), context_instance=RequestContext(request))
#
#
def imagem(request, slug):
    imgs = foto.objects.filter(album__slug=slug)
    context = {
        'imgs': imgs,
    }

    return render(request,'galeria/fotos.html',context)
