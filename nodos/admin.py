from django.contrib import admin
from nodos.models import Nodo, Destino


@admin.register(Nodo)
class NodoAdmin(admin.ModelAdmin):

    list_display= ('nombre', 'estado', 'direccion')

    search_fields = ('nombre',)

    list_display_links = ('nombre',)

    fieldsets = [
        ('Nodo', 
         
         {'fields': ['nombre', 'estado'],}, 
          
          ),

        ('Datos Generales',
           
          {'fields': ['telefono', 'calle', 'numero', 'localidad',]}, 
          
          ),
        
        ('Imagen maps',
        
          {'fields': ['mapa',]},
        
          ),
    
    ]

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):

    list_display= ('nombre', 'telefono', 'direccion')

    search_fields = ('nombre',)

    list_display_links = ('nombre',)

    fieldsets = [
        ('Nodo', 
         
         {'fields': ['nombre', 'estado'],}, 
          
          ),

         ('Datos Generales',
           
          {'fields': ['telefono', 'calle', 'numero', 'localidad',]}, 
          
          ),
            
        ('Imagen maps',
        
          {'fields': ['mapa',]},
        
          ),
    ]