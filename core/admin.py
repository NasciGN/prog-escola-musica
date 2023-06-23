from django.contrib import admin

from core.models import Muscico, Instrumento
# Register your models here.


@admin.register(Muscico)
class MusicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'dt_nascimento')
    list_filter = ('nome', 'nacionalidade')
    search_fields = ('nome', 'nacionalidade')


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'modelo', 'n_serie', 'musico')
    list_filter = ('nome', 'marca')
    search_fields = ('nome', 'marca', 'modelo', 'n_serie', 'musico')
