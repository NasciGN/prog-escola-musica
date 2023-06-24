from django.contrib import admin

from core.models import Apresentacao, Musico, Instrumento, Orquestra, Sinfonia

@admin.register(Musico)
class MusicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'dt_nascimento')
    list_filter = ('nome', 'nacionalidade')
    search_fields = ('nome', 'nacionalidade')


@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'modelo', 'n_serie', 'musico')
    list_filter = ('nome', 'marca')
    search_fields = ('nome', 'marca', 'modelo', 'n_serie', 'musico')


@admin.register(Sinfonia)
class SinfoniaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'compositor', 'dt_criacao')
    list_filter = ('nome', 'compositor')
    search_fields = ('nome', 'compositor')


@admin.register(Orquestra)
class OrquestraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'pais', 'mostrar_musicos')
    list_filter = ('nome', 'cidade')
    search_fields = ('nome', 'cidade')

    def mostrar_musicos(self, obj):
        return ", ".join([musico.nome for musico in obj.musicos.all()])
    
    mostrar_musicos.short_description = 'Músicos'


@admin.register(Apresentacao)
class ApresentacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'orquestra', 'sinfonia', 'dt_apresentacao')
    list_filter = ('nome', 'orquestra')
    search_fields = ('nome', 'orquestra', 'sinfonia', 'dt_apresentacao')