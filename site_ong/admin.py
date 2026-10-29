from django.contrib import admin

from .models import Projeto, Voluntario


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'periodo', 'horas']
    list_filter = ['periodo', 'projetos']
    search_fields = ['nome', 'email']
    filter_horizontal = ['projetos']


# textos do admin do Django (/admin-django/): topo, aba do navegador e pagina inicial
admin.site.site_header = 'Administração – Caminho da Esperança'
admin.site.site_title = 'Admin Caminho da Esperança'
admin.site.index_title = 'Painel de administração'
