from django.contrib import admin
from impresoras.models import ImpresoraNodo, ColaDeImpresion

@admin.register(ImpresoraNodo)
class EstadosAdmin(admin.ModelAdmin):

    list_display= ('nombre', 'nodo', 'estado',)

    search_fields = ('nombre',)

    list_display_links = ('nombre',)

@admin.register(ColaDeImpresion)
class EstadosAdmin(admin.ModelAdmin):

    list_display= ('trabajo', 'impresora', 'estado',)

    search_fields = ('trabajo',)

    list_display_links = ('trabajo',)
