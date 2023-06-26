from django import forms
from django.urls import reverse_lazy
from core.models import Musico
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class MusicoListView(LoginRequiredMixin, ListView):
    model = Musico
    template_name = 'musico/tabela_musico.html'
    context_object_name = 'musicos'
    login_url='login'

class MusicoCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Musico
    template_name = 'musico/criar_musico.html'
    fields = ['nome', 'nacionalidade', 'dt_nascimento']
    success_url = reverse_lazy('musico:read')
    login_url='login'
    permission_required = 'core.add_musico'

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ['nome', 'nacionalidade', 'dt_nascimento']
        widgets = {
            'dt_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class MusicoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Musico
    form_class = MusicoForm
    template_name = 'musico/criar_musico.html'
    success_url = reverse_lazy('musico:read')
    slug_field = 'id'
    login_url='login'
    permission_required = 'core.change_musico'


class MusicoDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Musico
    success_url = reverse_lazy('musico:read')
    login_url='login'
    permission_required = 'core.delete_musico'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


