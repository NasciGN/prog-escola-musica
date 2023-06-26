from django.urls import reverse_lazy
from core.models import Sinfonia
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class SinfoniaListView(LoginRequiredMixin, ListView):
    model = Sinfonia
    template_name = 'sinfonia/tabela_sinfonia.html'
    context_object_name = 'sinfonias'
    login_url='login'

class SinfoniaCreateView(LoginRequiredMixin, CreateView):
    model = Sinfonia
    template_name = 'sinfonia/criar_sinfonia.html'
    fields = ['nome', 'compositor',]
    success_url = reverse_lazy('sinfonia:read')
    login_url='login'

class SinfoniaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sinfonia
    template_name = 'sinfonia/criar_sinfonia.html'
    fields = ['nome', 'compositor']
    success_url = reverse_lazy('sinfonia:read')
    slug_field = 'id'
    login_url='login'

class SinfoniaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sinfonia
    success_url = reverse_lazy('sinfonia:read')
    login_url='login'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


