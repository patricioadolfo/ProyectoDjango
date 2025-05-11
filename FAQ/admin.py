from django.contrib import admin
from FAQ.models import PreguntasFrecuentes

@admin.register(PreguntasFrecuentes)
class FAQadmin(admin.ModelAdmin):

    list_display= ('titulo',)

    fieldsets = [
        ('Titulo', 
         
         {'fields': ['titulo'],}, 
          
          ),

        ('Contenido',
           
          {'fields': ['contenido',]}, 
          
          ),
    ]