from django.contrib import admin
from link.models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):

    list_display= ('nombre', 'url', 'estado',)

    search_fields = ('nombre',)

    list_display_links = ('nombre',)