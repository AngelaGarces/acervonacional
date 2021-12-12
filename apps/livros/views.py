from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.livros.models import Livros
from .forms import LivrosFormAdd


class LivrosList(ListView):
    model = Livros
   # context_object_name = ''  
    success_url = reverse_lazy('livros_listar')  
    template_name = 'livros_list.html'

class LivrosAdd(CreateView):
    model = Livros
    fields = ['nome']
    success_url = reverse_lazy('livros_listar')
    template_name = 'livros_form.html'
     #from_class = 'LivrosFormAdd'

class LivrosUpdate(UpdateView):
    model = Livros
    fields = ['nome']
    success_url = reverse_lazy('livros_listar')
    template_name = 'livros_update_form.html'
    

class LivrosDelete(DeleteView):
    model = Livros
    fields = ['nome']
    success_url = reverse_lazy('livros_listar')
    template_name = 'livros_confirm_delete_.html'
 