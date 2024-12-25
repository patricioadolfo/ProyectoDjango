from django.contrib import admin
from estados.models import Estado


@admin.register(Estado)
class EstadosAdmin(admin.ModelAdmin):

    list_display= ('id', 'color_estado',)

    search_fields = ('nombre',)

    list_display_links = ('id', 'color_estado',)
