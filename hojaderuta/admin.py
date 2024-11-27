from django.contrib import admin
from hojaderuta.models import Envio, SeguimientoDeEnvio

class SeguimientoDeEnvioInline(admin.TabularInline):
    
    model = SeguimientoDeEnvio

    extra = 0

@admin.register(Envio)
class RouteAdmin(admin.ModelAdmin):

    ordering = ['-id',]
    
    list_display = ('id', 'usuario', 'origen', 'otro_origen' , 'destino', 'otro_destino' , 'envio_estado',)

    search_fields = ('id',)

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
