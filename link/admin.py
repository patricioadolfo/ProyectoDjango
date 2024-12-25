from django.contrib import admin
from link.models import Links

@admin.register(Links)
class LinkAdmin(admin.ModelAdmin):

    list_display= ('nombre', 'url', 'ver_imagen','estado_link',)

    search_fields = ('nombre',)

    list_display_links = ('nombre',)
