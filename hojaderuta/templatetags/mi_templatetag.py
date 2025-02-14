from django import template
from farmacia.models import Parametros
from django.utils.html import format_html

parametro = Parametros()

register = template.Library()

@register.filter(name= 'ver_destino')
def ver_destino(envio):

    if envio.destino == None:

        return envio.otro_destino
    
    else:

        return envio.destino
    

@register.filter(name= 'cambio_estado')
def cambio_estado(envio, perfil):

    if envio.origen in perfil:

        if envio.estado == parametro.preparado:

            return format_html(
                """
                    <select name="estado" class="form-select">
                        <option value="{}">{}</option>
                    </select>
                    <br>
                    <input type="submit" value="OK" class="btn btn-primary btn-sm" id="btn_ok">
                
                """, parametro.ignorado.id, parametro.ignorado.nombre )
        
        else:
            
            return format_html('<p>No hay cambios de estados disponibles</p>')
    
    elif envio.destino in perfil:

        if envio.estado == parametro.en_camino:

            return format_html( 
                """
                    <select name="estado" class="form-select">
                        <option value="{}">{}</option>
                    </select>
                    <br>
                    <input type="submit" value="OK" class="btn btn-primary btn-sm" id="btn_ok">
                
                """, parametro.entregado.id, parametro.entregado.nombre )
        else:
            
            return format_html('<p>No hay cambios de estados disponibles</p>')

    else:
        return format_html('<p>No hay cambios de estados disponibles</p>')
    
