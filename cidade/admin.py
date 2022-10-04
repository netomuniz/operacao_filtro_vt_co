from django.contrib import admin
from . models import Estado, Cidade, Area


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ('us', 'estado')
    
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    search_fields = ('cidade', 'uf__estado')
    list_display = ('uf', 'cidade')
    list_per_page = 20

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    search_fields = ('area', 'cidade__cidade')
    list_display = ('cidade', 'area')
    list_per_page = 20
