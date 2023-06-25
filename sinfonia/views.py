from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from core.models import Sinfonia

# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView

class SinfoniaListView(ListView):
    model = Sinfonia
    template_name = 'sinfonia/tabela_sinfonia.html'
    context_object_name = 'sinfonias'

    
