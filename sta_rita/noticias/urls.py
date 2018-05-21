from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'noticias'


urlpatterns = [
    path('', views.newsList, name='NewsListView'),
    path('eventos/', views.eventosList, name='EventosListView'),
    url(r'^(?P<slug>[\w_-]+)/$', views.noticiaEspecifica, name='noticiaEspecifica'),
]