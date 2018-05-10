from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name="galeria"
urlpatterns = [
    path('', views.albuns, name='album1'),

    # /path('', views.albuns, name='album1'),

    url(r'^(?P<slug>[\w_-]+)/$', views.imagem, name='imagem'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)