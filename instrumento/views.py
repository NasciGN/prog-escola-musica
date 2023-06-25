from django.urls import reverse_lazy
from core.models import Instrumento
from django.shortcuts import redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

class InstrumentoListView(ListView):
    model = Instrumento
    template_name = 'instrumento/tabela_instrumento.html'
    context_object_name = 'instrumentos'

class InstrumentoCreateView(CreateView):
    model = Instrumento
    template_name = 'Instrumento/criar_Instrumento.html'
    fields = ['nome', 'marca', 'modelo', 'n_serie', 'musico']
    success_url = reverse_lazy('instrumento:read')

class InstrumentoUpdateView(UpdateView):
    model = Instrumento
    template_name = 'instrumento/criar_instrumento.html'
    fields = ['nome', 'marca', 'modelo', 'n_serie', 'musico']
    success_url = reverse_lazy('instrumento:read')
    slug_field = 'id'

class InstrumentoDeleteView(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('instrumento:read')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


