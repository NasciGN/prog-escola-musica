from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

class EscolaView(TemplateView):
    template_name = "table.html"



