from django.urls import reverse_lazy
from django.db.models.query import QuerySet
from django.shortcuts import render
from core.models import Sinfonia
from django.shortcuts import redirect

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
    slug_field = 'id'

class SinfoniaDeleteView(DeleteView):
    model = Sinfonia
    success_url = reverse_lazy('sinfonia:read')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


