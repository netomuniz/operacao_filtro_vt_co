from django.contrib import admin
from . models import Estado, Cidade, Area


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    pass

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass
