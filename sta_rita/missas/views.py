from django.shortcuts import render
from .models import Missa

# Create your views here.

def horarios(request):
    listaMissa = Missa.objects.all()
    context = {
        'listaMissa': listaMissa,
    }
    return render(request, 'missas/horarioDeMissas.html',context)

