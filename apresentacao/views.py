from django.urls import reverse_lazy
from core.models import Apresentacao
from django.shortcuts import redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

class ApresentacaoListView(ListView):
    model = Apresentacao
    template_name = 'apresentacao/tabela_apresentacao.html'
    context_object_name = 'apresentacoes'

class ApresentacaoCreateView(CreateView):
    model = Apresentacao
    template_name = 'apresentacao/criar_apresentacao.html'
    fields = ['nome', 'orquestra', 'sinfonia', 'dt_apresentacao', 'hr_apresentacao']
    success_url = reverse_lazy('apresentacao:read')

class ApresentacaoUpdateView(UpdateView):
    model = Apresentacao
    template_name = 'apresentacao/criar_apresentacao.html'
    fields = ['nome', 'orquestra', 'sinfonia', 'dt_apresentacao', 'hr_apresentacao']
    success_url = reverse_lazy('apresentacao:read')
    slug_field = 'id'

class ApresentacaoDeleteView(DeleteView):
    model = Apresentacao
    success_url = reverse_lazy('apresentacao:read')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


