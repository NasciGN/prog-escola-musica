from django.urls import reverse_lazy
from core.models import Musico
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

class MusicoListView(ListView):
    model = Musico
    template_name = 'musico/tabela_musico.html'
    context_object_name = 'musicos'

class MusicoCreateView(CreateView):
    model = Musico
    template_name = 'musico/criar_musico.html'
    fields = ['nome', 'nacionalidade', 'dt_nascimento']
    success_url = reverse_lazy('musico:read')

class MusicoUpdateView(UpdateView):
    model = Musico
    template_name = 'musico/criar_musico.html'
    fields = ['nome', 'nacionalidade', 'dt_nascimento']
    success_url = reverse_lazy('musico:read')
    slug_field = 'id'

class MusicoDeleteView(DeleteView):
    model = Musico
    success_url = reverse_lazy('musico:read')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


