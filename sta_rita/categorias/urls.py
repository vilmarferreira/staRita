from django.urls import path, include
from . import views
app_name="teste"
urlpatterns = [
    path('', views.index, name='albuns'),

]