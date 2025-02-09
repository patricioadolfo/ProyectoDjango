from django.contrib import admin
from perfiles.models import Perfil

@admin.register(Perfil)
class EstadosAdmin(admin.ModelAdmin):

    list_display= ('usuario', 'impresora', 'reparto')

    search_fields = ('usuario',)

    list_display_links = ('usuario',)
