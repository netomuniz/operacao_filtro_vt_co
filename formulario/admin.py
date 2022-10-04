from django.contrib import admin
from . models import TipoOs, TipoContato, GrupoProblema, DescricaoProblema, TipoSolucao, CodCancelamento


@admin.register(TipoOs)
class TipoOs(admin.ModelAdmin):   
    search_fields = ('tipo_os',) 
    list_per_page = 20

@admin.register(TipoContato)
class TipoContato(admin.ModelAdmin):
    search_fields = ('tipo_contato',) 
    list_per_page = 20

@admin.register(GrupoProblema)
class GrupoProblema(admin.ModelAdmin):
    search_fields = ('grupo_problema',) 
    list_per_page = 20

@admin.register(DescricaoProblema)
class DescricaoProblema(admin.ModelAdmin):
    list_display = ('grupo_problema', 'descricao_problema')
    search_fields = ('grupo_problema__grupo_problema', 'descricao_problema') 
    list_per_page = 20

@admin.register(TipoSolucao)
class TipoSolucao(admin.ModelAdmin):
    search_fields = ('tipo_solucao',) 
    list_per_page = 20

@admin.register(CodCancelamento)
class CodCancelamento(admin.ModelAdmin):
    search_fields = ('cod_cancelamento',) 
    list_per_page = 20
