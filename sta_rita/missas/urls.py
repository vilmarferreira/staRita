from django.urls import path
from . import views

app_name = 'missasHorarios'

urlpatterns = [
    path('missa', views.horarios, name='horariosMissa'),
]