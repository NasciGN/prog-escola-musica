from django.urls import reverse_lazy
from core.models import Orquestra
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class OrquestraListView(LoginRequiredMixin, ListView):
    model = Orquestra
    template_name = 'orquestra/tabela_orquestra.html'
    context_object_name = 'orquestras'
    login_url='login'

class OrquestraCreateView(LoginRequiredMixin, CreateView):
    model = Orquestra
    template_name = 'orquestra/criar_orquestra.html'
    fields = ['nome', 'cidade', 'pais', 'musicos']
    success_url = reverse_lazy('orquestra:read')
    login_url='login'
    

class OrquestraUpdateView(LoginRequiredMixin, UpdateView):
    model = Orquestra
    template_name = 'orquestra/criar_orquestra.html'
    fields = ['nome', 'cidade', 'pais', 'musicos']
    success_url = reverse_lazy('orquestra:read')
    slug_field = 'id'
    login_url='login'

class OrquestraDeleteView(LoginRequiredMixin, DeleteView):
    model = Orquestra
    success_url = reverse_lazy('orquestra:read')
    login_url='login'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


