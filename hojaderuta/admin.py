from django.contrib import admin
from hojaderuta.models import Envio, SeguimientoDeEnvio

class SeguimientoDeEnvioInline(admin.TabularInline):
    
    model = SeguimientoDeEnvio

    extra = 0

@admin.register(Envio)
class RouteAdmin(admin.ModelAdmin):

    ordering = ['-id',]
    
    list_display = ('envio_estado', 'usuario', 'origen', 'otro_origen' , 'destino', 'otro_destino',)

    search_fields = ('envio_estado',)

    fieldsets = [
        
        ('Datos Generales', 
            
            {'fields': 
            
                ['origen', 'otro_origen', 'destino', 'otro_destino', 'descripcion', 'estado'],
            
            },),
        
        ('Datos de Preparacion',
        
            {'fields': 
        
                ['usuario', 'fecha', 'hora',]
        
            },)
            
            ]
    
    inlines = [SeguimientoDeEnvioInline]
