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

                    <div class="col">
                        <select name="estado" class="form-control">
                            <option value="{}">{}</option>
                        </select>
                    </div>
                    <div class="col">
                        <input type="submit" value="OK" class="btn btn-primary btn-sm" id="btn_ok">
                    </div>

                """, parametro.ignorado.id, parametro.ignorado.nombre )
        
        else:
            
            return format_html('<p>No hay cambios de estados disponibles</p>')
    
    elif envio.destino in perfil:

        if envio.estado == parametro.en_camino:

            return format_html( 
                """

                    <div class="col">
                        <select name="estado" class="form-control">
                            <option value="{}">{}</option>
                        </select>
                    </div>
                    <div class="col">
                        <input type="submit" value="OK" class="btn btn-primary btn-sm" id="btn_ok">
                    </div>
                
                """, parametro.entregado.id, parametro.entregado.nombre )
        else:
            
            return format_html('<p>No hay cambios de estados disponibles</p>')

    else:
        return format_html('<p>No hay cambios de estados disponibles</p>')
    
@register.filter(name= 'class_form')
def class_form(form):

    for field in form:
        
        field.field.widget.attrs['style'] = "margin:5px;"
        
        field.field.widget.attrs['class'] = "form-control"

    return form

