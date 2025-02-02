from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from hojaderuta.models import Envio, SeguimientoDeEnvio
from farmacia.models import Parametros

class SeguimientoDeEnvioInline(admin.TabularInline):
    
    model = SeguimientoDeEnvio

    extra = 0

@admin.register(Envio)
class RouteAdmin(admin.ModelAdmin,):

    parametro = Parametros()

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

    def ignorar_envios( self, request, queryset ):

        registro = queryset.update( estado = self.parametro.ignorado )

        mensaje = "%s Envios ignorados" % registro

        self.message_user(request, mensaje)

    

    def ver_json( self, request, queryset ):

        response = HttpResponse( content_type = "application/json" )

        serializers.serialize( "json", queryset, stream = response )

        return response

    def ver_html( self, request, queryset ):
        
        self.parametro.params["envios"] = queryset

        return render( request, "admin/envios/envios.html", self.parametro.params )

    ignorar_envios.short_description = 'Ignorar Envio'

    ver_json.short_description = 'Exportar json'

    ver_html.short_description = 'Ver en html'

    actions = [ "ignorar_envios", "ver_json", "ver_html" ]