from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import render
from core.models import Sinfonia

from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView

class SinfoniaListView(ListView):
    model = Sinfonia
    template_name = 'sinfonia/tabela_sinfonia.html'
    context_object_name = 'sinfonias'

class SinfoniaCreateView(CreateView):
    model = Sinfonia
    template_name = 'sinfonia/criar_sinfonia.html'
    fields = ['nome', 'compositor',]
    success_url = reverse_lazy('sinfonia:read')

class SinfoniaUpdateView(UpdateView):
    model = Sinfonia
    template_name = 'sinfonia/criar_sinfonia.html'
    fields = ['nome', 'compositor']
    success_url = reverse_lazy('sinfonia:read')

class SinfoniaDeleteView(DeleteView):
    model = Sinfonia
    template_name = 'sinfonia/excluir_sinfonia.html'
    success_url = reverse_lazy('sinfonia:read')
