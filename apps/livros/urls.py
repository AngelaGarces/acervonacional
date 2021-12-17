from django.conf.urls import url
from django.urls import path

from apps.home.views import SobreView

from .views import LivrosList, LivrosAdd, LivrosDelete, LivrosUpdate
from django.views.generic.base import TemplateView


urlpatterns = [
    path('listar/', LivrosList.as_view(), name = 'livros_listar'),
    path('adicionar/', LivrosAdd.as_view(), name = 'adicionar_livros'),
    path('atualizar/<int:pk>', LivrosUpdate.as_view(), name= 'livros_atualizar'),
    path('deletar/<int:pk>', LivrosDelete.as_view(), name= 'livros_deletar'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]